"""Markdown card validation and Anki TSV generation for OpenAPlus."""

from __future__ import annotations

import csv
import html
import re
import shutil
import tempfile
from collections import defaultdict
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any

import markdown
import yaml
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode

CARD_TYPES = frozenset({"basic", "cloze", "image"})
DIFFICULTIES = frozenset({"easy", "medium", "hard"})
SUPPORTED_IMAGE_EXTENSIONS = frozenset({".svg", ".png", ".jpg", ".jpeg", ".webp"})
REQUIRED_METADATA = (
    "id",
    "exam",
    "objective",
    "objective_name",
    "type",
    "difficulty",
    "high_yield",
    "tags",
    "source",
)

_FRONT_MATTER = re.compile(
    r"\A---[ \t]*\r?\n(?P<yaml>.*?)^---[ \t]*\r?\n?(?P<body>.*)\Z",
    re.MULTILINE | re.DOTALL,
)
_HEADING = re.compile(r"^##[ \t]+(?P<name>.+?)[ \t]*$")
_FENCE_OPEN = re.compile(r"^[ ]{0,3}(?P<fence>`{3,}|~{3,})[^\r\n]*$")
_VALID_CLOZE = re.compile(r"\{\{c[1-9]\d*::[^{}\r\n]+\}\}")
_IMAGE_SOURCE = re.compile(r'<img\s+src="(?P<src>[^"]+)">')
_ID = re.compile(r"^(?P<objective>\d+(?:\.\d+)+)-(?P<kind>[BCI])(?P<number>\d{3})$")
_OBJECTIVE_DIRECTORY = re.compile(
    r"^(?P<objective>\d+(?:\.\d+)+)-[a-z0-9]+(?:-[a-z0-9]+)*$"
)
_INVALID_TAG_CHARACTERS = re.compile(r"[\s,]")
_RESERVED_TAG = re.compile(r"^A\+::")

_TYPE_LETTERS = {"basic": "B", "cloze": "C", "image": "I"}
_TYPE_TAGS = {"basic": "Basic", "cloze": "Cloze", "image": "Image"}
_SECTION_REQUIREMENTS = {
    "basic": ("Question", "Answer"),
    "cloze": ("Text",),
    "image": ("Prompt", "Answer"),
}
_TSV_HEADERS = {
    "basic": (
        "Card ID",
        "Front",
        "Back",
        "Instructor Notes",
        "Difficulty",
        "Card Type",
        "Objective",
        "Source",
        "Tags",
    ),
    "cloze": (
        "Card ID",
        "Text",
        "Extra",
        "Instructor Notes",
        "Difficulty",
        "Card Type",
        "Objective",
        "Source",
        "Tags",
    ),
    "image": (
        "Card ID",
        "Prompt",
        "Question Image",
        "Answer",
        "Answer Image",
        "Instructor Notes",
        "Difficulty",
        "Card Type",
        "Objective",
        "Source",
        "Tags",
    ),
}
_OUTPUT_NAMES = {"basic": "Basic.tsv", "cloze": "Cloze.tsv", "image": "Image.tsv"}


class ErrorCode(StrEnum):
    """Stable machine-readable validation error codes."""

    MISSING_METADATA = "OA001_MISSING_METADATA"
    DUPLICATE_ID = "OA002_DUPLICATE_ID"
    ID_FILENAME_MISMATCH = "OA003_ID_FILENAME_MISMATCH"
    INVALID_TYPE = "OA004_INVALID_TYPE"
    INVALID_DIFFICULTY = "OA005_INVALID_DIFFICULTY"
    MISSING_SECTION = "OA006_MISSING_SECTION"
    INVALID_CLOZE = "OA007_INVALID_CLOZE"
    MISSING_IMAGE = "OA008_MISSING_IMAGE"
    INVALID_TAG = "OA009_INVALID_TAG"
    PATH_METADATA_MISMATCH = "OA010_PATH_METADATA_MISMATCH"
    DUPLICATE_YAML_KEY = "OA011_DUPLICATE_YAML_KEY"
    INVALID_METADATA_TYPE = "OA012_INVALID_METADATA_TYPE"
    MANUAL_DERIVED_TAG = "OA013_MANUAL_DERIVED_TAG"
    INVALID_IMAGE_PATH = "OA014_INVALID_IMAGE_PATH"
    UNSUPPORTED_IMAGE_TYPE = "OA015_UNSUPPORTED_IMAGE_TYPE"
    INVALID_YAML = "OA016_INVALID_YAML"
    DUPLICATE_SECTION = "OA017_DUPLICATE_SECTION"
    NO_CARDS = "OA018_NO_CARDS"
    INVALID_MEDIA_REFERENCE = "OA019_INVALID_MEDIA_REFERENCE"


class WarningCode(StrEnum):
    """Stable machine-readable validation warning codes."""

    MISSING_INSTRUCTOR_NOTES = "OAW001_MISSING_INSTRUCTOR_NOTES"


@dataclass(frozen=True)
class Card:
    """A parsed source card."""

    path: Path
    metadata: dict[str, Any]
    sections: dict[str, str]


@dataclass(frozen=True)
class ValidationIssue:
    """One coded validation error or warning."""

    code: ErrorCode | WarningCode
    path: Path
    message: str


@dataclass
class ValidationResult:
    """Parsed cards and all validation findings."""

    cards: list[Card]
    errors: list[ValidationIssue]
    warnings: list[ValidationIssue]

    @property
    def valid(self) -> bool:
        return not self.errors


class CardParseError(ValueError):
    """Raised when a card cannot be parsed."""

    def __init__(self, code: ErrorCode, message: str) -> None:
        self.code = code
        super().__init__(message)


class DuplicateKeyError(ConstructorError):
    """Raised when YAML contains a duplicate mapping key."""


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def _construct_unique_mapping(
    loader: UniqueKeyLoader, node: MappingNode, deep: bool = False
) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError as error:
            raise ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found an unhashable key",
                key_node.start_mark,
            ) from error
        if duplicate:
            raise DuplicateKeyError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key: {key}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping
)


def discover_card_files(content_root: Path) -> list[Path]:
    """Return card Markdown files in deterministic order."""

    if not content_root.exists():
        return []
    return sorted(
        path for path in content_root.rglob("*.md") if path.parent.name == "cards"
    )


def parse_card(path: Path) -> Card:
    """Parse one card file without applying semantic validation."""

    text = path.read_text(encoding="utf-8")
    match = _FRONT_MATTER.match(text)
    if match is None:
        raise CardParseError(
            ErrorCode.INVALID_YAML, "missing or malformed YAML front matter"
        )

    try:
        metadata = yaml.load(match.group("yaml"), Loader=UniqueKeyLoader)
    except DuplicateKeyError as error:
        raise CardParseError(ErrorCode.DUPLICATE_YAML_KEY, str(error)) from error
    except yaml.YAMLError as error:
        raise CardParseError(
            ErrorCode.INVALID_YAML, f"invalid YAML front matter: {error}"
        ) from error
    if not isinstance(metadata, dict):
        raise CardParseError(
            ErrorCode.INVALID_YAML, "YAML front matter must be a mapping"
        )

    sections = _parse_sections(match.group("body"))
    return Card(path=path, metadata=metadata, sections=sections)


def _parse_sections(body: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_name: str | None = None
    current_lines: list[str] = []
    active_fence: tuple[str, int] | None = None

    def finish_section() -> None:
        nonlocal current_lines
        if current_name is not None:
            sections[current_name] = "".join(current_lines).strip()
        current_lines = []

    for line in body.splitlines(keepends=True):
        line_without_ending = line.rstrip("\r\n")
        fence = _FENCE_OPEN.match(line_without_ending)
        if active_fence is not None:
            if current_name is not None:
                current_lines.append(line)
            character, minimum_length = active_fence
            closing = re.fullmatch(
                rf"[ ]{{0,3}}{re.escape(character)}{{{minimum_length},}}[ \t]*",
                line_without_ending,
            )
            if closing:
                active_fence = None
            continue
        if fence:
            marker = fence.group("fence")
            active_fence = (marker[0], len(marker))
            if current_name is not None:
                current_lines.append(line)
            continue

        heading = _HEADING.match(line_without_ending)
        if heading:
            finish_section()
            name = heading.group("name").strip()
            if name in sections:
                raise CardParseError(
                    ErrorCode.DUPLICATE_SECTION, f"duplicate section heading: {name}"
                )
            current_name = name
        elif current_name is not None:
            current_lines.append(line)

    finish_section()
    return sections


def validate_cards(content_root: Path, repository_root: Path) -> ValidationResult:
    """Parse and validate every card below ``content_root``."""

    cards: list[Card] = []
    errors: list[ValidationIssue] = []
    warnings: list[ValidationIssue] = []
    ids: dict[str, Path] = {}
    objective_names: dict[Path, tuple[str, Path]] = {}
    media_names: dict[str, Path] = {}
    repository_root = repository_root.resolve()
    content_root = content_root.resolve()

    files = discover_card_files(content_root)
    if not files:
        errors.append(
            ValidationIssue(ErrorCode.NO_CARDS, content_root, "no card files found")
        )
        return ValidationResult(cards, errors, warnings)

    for path in files:
        try:
            card = parse_card(path)
        except CardParseError as error:
            errors.append(ValidationIssue(error.code, path, str(error)))
            continue
        except (OSError, UnicodeError) as error:
            errors.append(ValidationIssue(ErrorCode.INVALID_YAML, path, str(error)))
            continue

        cards.append(card)
        _validate_required_metadata(card, errors)
        _validate_identity_and_path(card, content_root, ids, errors)
        _validate_sections(card, errors, warnings)
        _validate_tags(card, errors)
        _validate_images(card, repository_root, media_names, errors)
        _validate_objective_name_consistency(card, objective_names, errors)

    return ValidationResult(cards, errors, warnings)


def _validate_required_metadata(card: Card, errors: list[ValidationIssue]) -> None:
    metadata = card.metadata
    for field in REQUIRED_METADATA:
        if field not in metadata:
            errors.append(
                ValidationIssue(
                    ErrorCode.MISSING_METADATA,
                    card.path,
                    f"missing required metadata: {field}",
                )
            )

    for field in ("id", "exam", "objective", "objective_name", "type", "difficulty"):
        if field in metadata and (
            not isinstance(metadata[field], str) or not metadata[field].strip()
        ):
            errors.append(
                ValidationIssue(
                    ErrorCode.INVALID_METADATA_TYPE,
                    card.path,
                    f"metadata '{field}' must be a non-empty string",
                )
            )

    if "high_yield" in metadata and not isinstance(metadata["high_yield"], bool):
        errors.append(
            ValidationIssue(
                ErrorCode.INVALID_METADATA_TYPE,
                card.path,
                "metadata 'high_yield' must be a boolean",
            )
        )

    for field in ("tags", "source"):
        value = metadata.get(field)
        if field in metadata and (
            not isinstance(value, list)
            or not value
            or any(not isinstance(item, str) or not item.strip() for item in value)
        ):
            errors.append(
                ValidationIssue(
                    ErrorCode.INVALID_METADATA_TYPE,
                    card.path,
                    f"metadata '{field}' must be a non-empty list of strings",
                )
            )

    card_type = metadata.get("type")
    if isinstance(card_type, str) and card_type not in CARD_TYPES:
        errors.append(
            ValidationIssue(
                ErrorCode.INVALID_TYPE,
                card.path,
                f"invalid card type '{card_type}'; "
                f"expected one of {sorted(CARD_TYPES)}",
            )
        )
    difficulty = metadata.get("difficulty")
    if isinstance(difficulty, str) and difficulty not in DIFFICULTIES:
        errors.append(
            ValidationIssue(
                ErrorCode.INVALID_DIFFICULTY,
                card.path,
                f"invalid difficulty '{difficulty}'; "
                f"expected one of {sorted(DIFFICULTIES)}",
            )
        )


def _validate_identity_and_path(
    card: Card,
    content_root: Path,
    ids: dict[str, Path],
    errors: list[ValidationIssue],
) -> None:
    metadata = card.metadata
    card_id = metadata.get("id")
    if not isinstance(card_id, str) or not card_id:
        return
    if card.path.stem != card_id:
        errors.append(
            ValidationIssue(
                ErrorCode.ID_FILENAME_MISMATCH,
                card.path,
                f"card id '{card_id}' does not match filename '{card.path.stem}'",
            )
        )
    if card_id in ids:
        errors.append(
            ValidationIssue(
                ErrorCode.DUPLICATE_ID,
                card.path,
                f"duplicate card id '{card_id}' (first in {ids[card_id]})",
            )
        )
    else:
        ids[card_id] = card.path

    id_match = _ID.fullmatch(card_id)
    if id_match is None:
        errors.append(
            ValidationIssue(
                ErrorCode.PATH_METADATA_MISMATCH,
                card.path,
                "card id must match '<objective>-[B|C|I]<three digits>'",
            )
        )
        return

    card_type = metadata.get("type")
    if (
        isinstance(card_type, str)
        and card_type in _TYPE_LETTERS
        and id_match.group("kind") != _TYPE_LETTERS[card_type]
    ):
        errors.append(
            ValidationIssue(
                ErrorCode.PATH_METADATA_MISMATCH,
                card.path,
                f"card id type letter does not match type '{card_type}'",
            )
        )
    objective = metadata.get("objective")
    if isinstance(objective, str) and id_match.group("objective") != objective:
        errors.append(
            ValidationIssue(
                ErrorCode.PATH_METADATA_MISMATCH,
                card.path,
                "card id objective does not match metadata objective",
            )
        )

    try:
        relative = card.path.resolve().relative_to(content_root)
    except ValueError:
        errors.append(
            ValidationIssue(
                ErrorCode.PATH_METADATA_MISMATCH,
                card.path,
                "card path is outside the content root",
            )
        )
        return
    if len(relative.parts) < 5:
        errors.append(
            ValidationIssue(
                ErrorCode.PATH_METADATA_MISMATCH,
                card.path,
                "card path must include exam/objective/cards directories",
            )
        )
        return

    path_exam = relative.parts[-4]
    objective_directory = relative.parts[-3]
    directory_match = _OBJECTIVE_DIRECTORY.fullmatch(objective_directory)
    if metadata.get("exam") != path_exam:
        errors.append(
            ValidationIssue(
                ErrorCode.PATH_METADATA_MISMATCH,
                card.path,
                f"path exam '{path_exam}' does not match metadata exam",
            )
        )
    if directory_match is None:
        errors.append(
            ValidationIssue(
                ErrorCode.PATH_METADATA_MISMATCH,
                card.path,
                f"invalid objective directory name: {objective_directory}",
            )
        )
    elif directory_match.group("objective") != metadata.get("objective"):
        errors.append(
            ValidationIssue(
                ErrorCode.PATH_METADATA_MISMATCH,
                card.path,
                "objective directory does not match metadata objective",
            )
        )


def _validate_sections(
    card: Card,
    errors: list[ValidationIssue],
    warnings: list[ValidationIssue],
) -> None:
    card_type = card.metadata.get("type")
    if isinstance(card_type, str) and card_type in _SECTION_REQUIREMENTS:
        for section in _SECTION_REQUIREMENTS[card_type]:
            if not card.sections.get(section):
                errors.append(
                    ValidationIssue(
                        ErrorCode.MISSING_SECTION,
                        card.path,
                        f"missing or empty section: ## {section}",
                    )
                )
    if card_type == "cloze":
        text = card.sections.get("Text", "")
        if not _has_only_valid_clozes(text):
            errors.append(
                ValidationIssue(
                    ErrorCode.INVALID_CLOZE,
                    card.path,
                    "## Text must contain only valid clozes such as {{c1::answer}}",
                )
            )
    if not card.sections.get("Instructor Notes"):
        warnings.append(
            ValidationIssue(
                WarningCode.MISSING_INSTRUCTOR_NOTES,
                card.path,
                "missing recommended section: ## Instructor Notes",
            )
        )


def _has_only_valid_clozes(text: str) -> bool:
    valid_clozes = list(_VALID_CLOZE.finditer(text))
    if not valid_clozes:
        return False
    valid_starts = {match.start() for match in valid_clozes}
    valid_ends = {match.end() - 2 for match in valid_clozes}
    opening_starts = {
        index for index in range(len(text) - 1) if text[index : index + 2] == "{{"
    }
    closing_starts = {
        index for index in range(len(text) - 1) if text[index : index + 2] == "}}"
    }
    return opening_starts == valid_starts and closing_starts == valid_ends


def normalize_objective_name(value: str) -> str:
    """Normalize an objective name for use in a hierarchical Anki tag."""

    return re.sub(r"[^A-Za-z0-9]", "", value)


def derived_tags(metadata: dict[str, Any]) -> list[str]:
    """Return deterministic structural tags derived from validated metadata."""

    tags = [
        f"A+::{metadata['exam']}::{metadata['objective']}",
        f"A+::{metadata['exam']}::{normalize_objective_name(metadata['objective_name'])}",
        _TYPE_TAGS[metadata["type"]],
    ]
    if metadata["high_yield"]:
        tags.append("HighYield")
    return tags


def final_tags(metadata: dict[str, Any]) -> list[str]:
    """Combine derived and custom tags without duplicates."""

    ordered: list[str] = []
    seen: set[str] = set()
    for tag in [*derived_tags(metadata), *metadata["tags"]]:
        if tag not in seen:
            ordered.append(tag)
            seen.add(tag)
    return ordered


def rendered_objective(metadata: dict[str, Any]) -> str:
    """Return the Anki display value for the Objective field."""

    return f"{metadata['exam']} {metadata['objective']} - {metadata['objective_name']}"


def _validate_tags(card: Card, errors: list[ValidationIssue]) -> None:
    tags = card.metadata.get("tags")
    if not isinstance(tags, list):
        return
    for tag in tags:
        if not isinstance(tag, str):
            continue
        if not tag or _INVALID_TAG_CHARACTERS.search(tag):
            errors.append(
                ValidationIssue(
                    ErrorCode.INVALID_TAG,
                    card.path,
                    f"custom tag contains whitespace, a comma, or is empty: {tag!r}",
                )
            )
        if _RESERVED_TAG.match(tag) or tag in {*_TYPE_TAGS.values(), "HighYield"}:
            errors.append(
                ValidationIssue(
                    ErrorCode.MANUAL_DERIVED_TAG,
                    card.path,
                    f"authors must not provide derived tag: {tag}",
                )
            )
    objective_name = card.metadata.get("objective_name")
    if isinstance(objective_name, str) and not normalize_objective_name(objective_name):
        errors.append(
            ValidationIssue(
                ErrorCode.INVALID_TAG,
                card.path,
                "objective_name must contain characters usable in a derived tag",
            )
        )


def _validate_images(
    card: Card,
    repository_root: Path,
    media_names: dict[str, Path],
    errors: list[ValidationIssue],
) -> None:
    if card.metadata.get("type") != "image":
        return
    approved_root = (repository_root / "assets" / "diagrams").resolve()
    for field in ("question_image", "answer_image"):
        value = card.metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(
                ValidationIssue(
                    ErrorCode.MISSING_IMAGE,
                    card.path,
                    f"missing or invalid image metadata: {field}",
                )
            )
            continue
        source_path = Path(value)
        if source_path.is_absolute() or ".." in source_path.parts:
            errors.append(
                ValidationIssue(
                    ErrorCode.INVALID_IMAGE_PATH,
                    card.path,
                    f"image path must be relative without traversal: {value}",
                )
            )
            continue
        image_path = (repository_root / value).resolve()
        if not image_path.is_relative_to(approved_root):
            errors.append(
                ValidationIssue(
                    ErrorCode.INVALID_IMAGE_PATH,
                    card.path,
                    f"image must stay inside assets/diagrams: {value}",
                )
            )
            continue
        if image_path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
            errors.append(
                ValidationIssue(
                    ErrorCode.UNSUPPORTED_IMAGE_TYPE,
                    card.path,
                    f"unsupported image type: {image_path.suffix or '<none>'}",
                )
            )
        if not image_path.is_file():
            errors.append(
                ValidationIssue(
                    ErrorCode.MISSING_IMAGE,
                    card.path,
                    f"image file does not exist: {value}",
                )
            )
            continue
        previous = media_names.get(image_path.name)
        if previous is not None and previous != image_path:
            errors.append(
                ValidationIssue(
                    ErrorCode.INVALID_IMAGE_PATH,
                    card.path,
                    f"image basename collides in Anki media: {image_path.name}",
                )
            )
        else:
            media_names[image_path.name] = image_path


def _validate_objective_name_consistency(
    card: Card,
    objective_names: dict[Path, tuple[str, Path]],
    errors: list[ValidationIssue],
) -> None:
    value = card.metadata.get("objective_name")
    if not isinstance(value, str) or not value.strip():
        return
    objective_directory = card.path.resolve().parent.parent
    previous = objective_names.get(objective_directory)
    if previous is not None and previous[0] != value:
        errors.append(
            ValidationIssue(
                ErrorCode.PATH_METADATA_MISMATCH,
                card.path,
                f"objective_name differs from {previous[1]}",
            )
        )
    else:
        objective_names[objective_directory] = (value, card.path)


def markdown_to_html(value: str) -> str:
    """Convert one Markdown card field to Anki-compatible HTML."""

    return markdown.markdown(
        value,
        extensions=["fenced_code", "sane_lists"],
        output_format="html5",
    )


def generate_tsv(
    cards: list[Card], content_root: Path, output_root: Path
) -> list[Path]:
    """Build the complete TSV tree and replace the previous output atomically."""

    grouped: dict[tuple[str, str, str], list[Card]] = defaultdict(list)
    content_root = content_root.resolve()
    for card in cards:
        relative_path = card.path.resolve().relative_to(content_root)
        objective_directory = relative_path.parent.parent.name
        key = (
            str(card.metadata["exam"]),
            objective_directory,
            str(card.metadata["type"]),
        )
        grouped[key].append(card)

    output_root = output_root.resolve()
    output_root.parent.mkdir(parents=True, exist_ok=True)
    temporary_root = Path(
        tempfile.mkdtemp(prefix=f".{output_root.name}-", dir=output_root.parent)
    )
    backup_root: Path | None = None
    try:
        relative_outputs: list[Path] = []
        for (exam, objective_directory, card_type), group in sorted(grouped.items()):
            relative_output = (
                Path(exam) / objective_directory / _OUTPUT_NAMES[card_type]
            )
            destination = temporary_root / relative_output
            destination.parent.mkdir(parents=True, exist_ok=True)
            _write_tsv(destination, card_type, group)
            relative_outputs.append(relative_output)

        if output_root.exists():
            backup_root = output_root.with_name(f".{output_root.name}-previous")
            if backup_root.exists():
                shutil.rmtree(backup_root)
            output_root.replace(backup_root)
        try:
            temporary_root.replace(output_root)
        except OSError:
            if backup_root is not None and backup_root.exists():
                backup_root.replace(output_root)
            raise
        if backup_root is not None:
            shutil.rmtree(backup_root)
        return [output_root / path for path in relative_outputs]
    finally:
        if temporary_root.exists():
            shutil.rmtree(temporary_root)


def _write_tsv(destination: Path, card_type: str, cards: list[Card]) -> None:
    headers = _TSV_HEADERS[card_type]
    columns = "\t".join(headers)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        handle.write("#separator:Tab\n")
        handle.write("#html:true\n")
        handle.write(f"#tags column:{len(headers)}\n")
        handle.write(f"#columns:{columns}\n")
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        for card in sorted(cards, key=lambda item: str(item.metadata["id"])):
            writer.writerow(_tsv_row(card, card_type))


def _tsv_row(card: Card, card_type: str) -> tuple[str, ...]:
    metadata = card.metadata
    card_id = str(metadata["id"])
    common = (
        str(metadata["difficulty"]),
        str(metadata["type"]),
        rendered_objective(metadata),
        "; ".join(metadata["source"]),
        " ".join(final_tags(metadata)),
    )
    notes = markdown_to_html(card.sections.get("Instructor Notes", ""))

    if card_type == "basic":
        return (
            card_id,
            markdown_to_html(card.sections["Question"]),
            markdown_to_html(card.sections["Answer"]),
            notes,
            *common,
        )
    if card_type == "cloze":
        return (
            card_id,
            markdown_to_html(card.sections["Text"]),
            markdown_to_html(card.sections.get("Extra", "")),
            notes,
            *common,
        )
    return (
        card_id,
        markdown_to_html(card.sections["Prompt"]),
        _image_reference(card, "question_image"),
        markdown_to_html(card.sections["Answer"]),
        _image_reference(card, "answer_image"),
        notes,
        *common,
    )


def media_filename(card: Card, field: str) -> str:
    """Return the deterministic staged Anki media filename for one image field."""

    suffix = Path(str(card.metadata[field])).suffix.lower()
    role = "question" if field == "question_image" else "answer"
    return f"{card.metadata['id']}-{role}{suffix}"


def _image_reference(card: Card, field: str) -> str:
    filename = media_filename(card, field)
    return f'<img src="{html.escape(filename, quote=True)}">'


def build_media(
    cards: list[Card], content_root: Path, repository_root: Path, media_root: Path
) -> list[Path]:
    """Stage image-card media into the complete output media tree atomically."""

    content_root = content_root.resolve()
    repository_root = repository_root.resolve()
    media_root = media_root.resolve()
    media_root.parent.mkdir(parents=True, exist_ok=True)
    temporary_root = Path(
        tempfile.mkdtemp(prefix=f".{media_root.name}-", dir=media_root.parent)
    )
    backup_root: Path | None = None
    try:
        relative_outputs: list[Path] = []
        for card in sorted(cards, key=lambda item: str(item.metadata["id"])):
            if card.metadata.get("type") != "image":
                continue
            relative_path = card.path.resolve().relative_to(content_root)
            objective_directory = relative_path.parent.parent.name
            exam = str(card.metadata["exam"])
            for field in ("question_image", "answer_image"):
                source = (repository_root / str(card.metadata[field])).resolve()
                relative_output = (
                    Path(exam) / objective_directory / media_filename(card, field)
                )
                destination = temporary_root / relative_output
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
                relative_outputs.append(relative_output)

        if media_root.exists():
            backup_root = media_root.with_name(f".{media_root.name}-previous")
            if backup_root.exists():
                shutil.rmtree(backup_root)
            media_root.replace(backup_root)
        try:
            temporary_root.replace(media_root)
        except OSError:
            if backup_root is not None and backup_root.exists():
                backup_root.replace(media_root)
            raise
        if backup_root is not None:
            shutil.rmtree(backup_root)
        return [media_root / path for path in relative_outputs]
    finally:
        if temporary_root.exists():
            shutil.rmtree(temporary_root)


def validate_generated_media(tsv_root: Path, media_root: Path) -> list[ValidationIssue]:
    """Validate that generated Image TSV references match staged media files."""

    tsv_root = tsv_root.resolve()
    media_root = media_root.resolve()
    errors: list[ValidationIssue] = []
    referenced: set[Path] = set()

    for image_tsv in sorted(tsv_root.rglob("Image.tsv")):
        try:
            relative_directory = image_tsv.parent.relative_to(tsv_root)
        except ValueError:
            relative_directory = Path()
        media_directory = media_root / relative_directory
        with image_tsv.open(encoding="utf-8", newline="") as handle:
            for _ in range(4):
                handle.readline()
            reader = csv.reader(handle, delimiter="\t")
            for row_number, row in enumerate(reader, start=5):
                if len(row) < 5:
                    continue
                for value in (row[2], row[4]):
                    match = _IMAGE_SOURCE.fullmatch(value.strip())
                    if match is None:
                        errors.append(
                            ValidationIssue(
                                ErrorCode.INVALID_MEDIA_REFERENCE,
                                image_tsv,
                                f"row {row_number} has invalid image HTML: {value}",
                            )
                        )
                        continue
                    src = match.group("src")
                    source_path = Path(src)
                    if (
                        source_path.name != src
                        or source_path.is_absolute()
                        or ".." in source_path.parts
                        or "assets" in source_path.parts
                    ):
                        message = (
                            f"row {row_number} image reference is not "
                            f"filename-only: {src}"
                        )
                        errors.append(
                            ValidationIssue(
                                ErrorCode.INVALID_MEDIA_REFERENCE,
                                image_tsv,
                                message,
                            )
                        )
                        continue
                    destination = media_directory / src
                    referenced.add(destination)
                    if not destination.is_file():
                        errors.append(
                            ValidationIssue(
                                ErrorCode.MISSING_IMAGE,
                                image_tsv,
                                f"TSV references missing staged media file: {src}",
                            )
                        )

    actual = (
        {path for path in media_root.rglob("*") if path.is_file()}
        if media_root.exists()
        else set()
    )
    for path in sorted(actual - referenced):
        errors.append(
            ValidationIssue(
                ErrorCode.INVALID_MEDIA_REFERENCE,
                path,
                "staged media file is not referenced by generated Image.tsv",
            )
        )
    return errors


def format_issue(issue: ValidationIssue, repository_root: Path) -> str:
    """Format a coded issue with a repository-relative path when possible."""

    try:
        path = issue.path.resolve().relative_to(repository_root.resolve())
    except ValueError:
        path = issue.path
    return f"{issue.code} {path}: {issue.message}"
