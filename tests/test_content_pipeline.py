from __future__ import annotations

import csv
import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

import openaplus.content_pipeline as pipeline
from openaplus.content_pipeline import (
    ErrorCode,
    build_media,
    derived_tags,
    final_tags,
    final_tags_for_card,
    generate_tsv,
    markdown_to_html,
    parse_card,
    validate_cards,
    validate_generated_media,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BASIC_BODY = """\
## Question

What is the answer?

## Answer

The **answer**.

## Instructor Notes

Minimal test note.
"""
BASIC_BODY_WITH_HINT = BASIC_BODY.replace(
    "## Answer",
    "## Hint\n\nThink about the test fixture.\n\n## Answer",
)
CLOZE_BODY = """\
## Text

The answer is {{c1::here}}.

## Extra

Minimal context.

## Instructor Notes

Minimal test note.
"""
IMAGE_BODY = """\
## Prompt

Identify the item.

## Answer

The item.

## Instructor Notes

Minimal test note.
"""
COMMAND_BODY = """\
## Prompt

Which command launches the tool?

## Typed Answer

tool.exe

## Back

The command launches the tool.

## Instructor Notes

Minimal test note.
"""


def metadata(card_id: str = "1.1-B001", card_type: str = "basic") -> dict[str, object]:
    return {
        "id": card_id,
        "exam": "220-1201",
        "objective": "1.1",
        "objective_name": "Laptop Hardware",
        "type": card_type,
        "difficulty": "easy",
        "high_yield": True,
        "tags": ["Memory", "Scenario"],
        "source": ["Test fixture"],
    }


def write_card(
    repository: Path,
    card_metadata: dict[str, object],
    body: str,
    *,
    filename: str | None = None,
    exam_directory: str = "220-1201",
    objective_directory: str = "1.1-laptop-hardware",
) -> Path:
    cards = (
        repository
        / "content"
        / "comptia"
        / "aplus"
        / exam_directory
        / objective_directory
        / "cards"
    )
    cards.mkdir(parents=True, exist_ok=True)
    path = cards / (filename or f"{card_metadata['id']}.md")
    front_matter = yaml.safe_dump(card_metadata, sort_keys=False).strip()
    path.write_text(f"---\n{front_matter}\n---\n\n{body}", encoding="utf-8")
    return path


def create_image(repository: Path, name: str) -> str:
    path = repository / "assets" / "diagrams" / "220-1201" / "1.1" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("<svg/>", encoding="utf-8")
    return path.relative_to(repository).as_posix()


def image_metadata(repository: Path) -> dict[str, object]:
    card_metadata = metadata("1.1-I001", "image")
    card_metadata["question_image"] = create_image(repository, "question.svg")
    card_metadata["answer_image"] = create_image(repository, "answer.svg")
    return card_metadata


def validate(repository: Path):
    return validate_cards(repository / "content", repository)


def error_codes(repository: Path) -> list[ErrorCode]:
    return [issue.code for issue in validate(repository).errors]


def read_tsv(path: Path) -> tuple[list[str], list[list[str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        comments = [handle.readline().rstrip("\n") for _ in range(4)]
        rows = list(csv.reader(handle, delimiter="\t"))
    columns = comments[3].removeprefix("#columns:").split("\t")
    return columns, rows, comments


def generated_files(repository: Path) -> dict[str, Path]:
    result = validate(repository)
    assert result.valid
    output = repository / "output" / "tsv"
    paths = generate_tsv(result.cards, repository / "content", output)
    return {path.name: path for path in paths}


def generated_outputs(repository: Path) -> tuple[dict[str, Path], list[Path]]:
    result = validate(repository)
    assert result.valid
    output = repository / "output" / "tsv"
    media = repository / "output" / "media"
    tsv_paths = generate_tsv(result.cards, repository / "content", output)
    media_paths = build_media(result.cards, repository / "content", repository, media)
    errors = validate_generated_media(output, media)
    assert not errors
    return {path.name: path for path in tsv_paths}, media_paths


def test_valid_basic_cloze_image_and_command_cards(tmp_path: Path) -> None:
    write_card(tmp_path, metadata(), BASIC_BODY)
    write_card(tmp_path, metadata("1.1-C001", "cloze"), CLOZE_BODY)
    write_card(tmp_path, image_metadata(tmp_path), IMAGE_BODY)
    write_card(tmp_path, metadata("1.1-T001", "command"), COMMAND_BODY)

    result = validate(tmp_path)

    assert result.valid
    assert len(result.cards) == 4


def test_duplicate_id_detection(tmp_path: Path) -> None:
    card_metadata = metadata()
    write_card(tmp_path, card_metadata, BASIC_BODY)
    write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="1.1-secondary-sample",
    )

    assert ErrorCode.DUPLICATE_ID in error_codes(tmp_path)


def test_same_objective_card_id_can_repeat_across_exams(tmp_path: Path) -> None:
    write_card(tmp_path, metadata(), BASIC_BODY)
    core2_metadata = metadata()
    core2_metadata["exam"] = "220-1202"
    core2_metadata["objective_name"] = "Operating System Types and Purposes"
    write_card(
        tmp_path,
        core2_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.1-operating-system-types-and-purposes",
    )

    assert validate(tmp_path).valid


def test_missing_required_metadata(tmp_path: Path) -> None:
    card_metadata = metadata()
    del card_metadata["source"]
    write_card(tmp_path, card_metadata, BASIC_BODY)

    assert ErrorCode.MISSING_METADATA in error_codes(tmp_path)


def test_missing_required_section_has_stable_code(tmp_path: Path) -> None:
    write_card(tmp_path, metadata(), BASIC_BODY.replace("## Answer", "## Explanation"))

    assert ErrorCode.MISSING_SECTION in error_codes(tmp_path)


@pytest.mark.parametrize(
    ("field", "value", "code"),
    [
        ("difficulty", "expert", ErrorCode.INVALID_DIFFICULTY),
        ("type", "multiple-choice", ErrorCode.INVALID_TYPE),
        ("high_yield", "yes", ErrorCode.INVALID_METADATA_TYPE),
        ("tags", "Memory", ErrorCode.INVALID_METADATA_TYPE),
        ("source", "Fixture", ErrorCode.INVALID_METADATA_TYPE),
        ("exam", 2201201, ErrorCode.INVALID_METADATA_TYPE),
    ],
)
def test_invalid_metadata_types_and_values(
    tmp_path: Path, field: str, value: object, code: ErrorCode
) -> None:
    card_metadata = metadata()
    card_metadata[field] = value
    write_card(tmp_path, card_metadata, BASIC_BODY)

    assert code in error_codes(tmp_path)


def test_duplicate_yaml_keys_are_rejected(tmp_path: Path) -> None:
    path = write_card(tmp_path, metadata(), BASIC_BODY)
    text = path.read_text(encoding="utf-8")
    path.write_text(
        text.replace("id: 1.1-B001", "id: 1.1-B001\nid: 1.1-B002"), encoding="utf-8"
    )

    assert error_codes(tmp_path) == [ErrorCode.DUPLICATE_YAML_KEY]


@pytest.mark.parametrize(
    ("metadata_updates", "filename", "exam_directory", "objective_directory"),
    [
        ({"id": "1.1-C001", "type": "basic"}, None, "220-1201", "1.1-laptop-hardware"),
        ({"objective": "1.2"}, None, "220-1201", "1.1-laptop-hardware"),
        ({"exam": "220-1202"}, None, "220-1201", "1.1-laptop-hardware"),
        ({}, "1.1-B999.md", "220-1201", "1.1-laptop-hardware"),
    ],
)
def test_metadata_path_and_id_consistency(
    tmp_path: Path,
    metadata_updates: dict[str, object],
    filename: str | None,
    exam_directory: str,
    objective_directory: str,
) -> None:
    card_metadata = metadata()
    card_metadata.update(metadata_updates)
    write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        filename=filename,
        exam_directory=exam_directory,
        objective_directory=objective_directory,
    )

    codes = error_codes(tmp_path)
    assert (
        ErrorCode.PATH_METADATA_MISMATCH in codes
        or ErrorCode.ID_FILENAME_MISMATCH in codes
    )


def test_objective_name_must_be_consistent(tmp_path: Path) -> None:
    write_card(tmp_path, metadata(), BASIC_BODY)
    second = metadata("1.1-B002")
    second["objective_name"] = "Different Name"
    write_card(tmp_path, second, BASIC_BODY)

    assert ErrorCode.PATH_METADATA_MISMATCH in error_codes(tmp_path)


@pytest.mark.parametrize("tag", ["two words", "tab\ttag", "comma,tag", ""])
def test_invalid_custom_tags_are_rejected(tmp_path: Path, tag: str) -> None:
    card_metadata = metadata()
    card_metadata["tags"] = [tag]
    write_card(tmp_path, card_metadata, BASIC_BODY)

    codes = error_codes(tmp_path)
    assert ErrorCode.INVALID_TAG in codes or ErrorCode.INVALID_METADATA_TYPE in codes


@pytest.mark.parametrize(
    "tag",
    [
        "A+::220-1201::1.1",
        "A+::220-1201::LaptopHardware",
        "Basic",
        "HighYield",
        "Source::Messer-v170",
    ],
)
def test_manual_derived_tags_are_rejected(tmp_path: Path, tag: str) -> None:
    card_metadata = metadata()
    card_metadata["tags"] = [tag]
    write_card(tmp_path, card_metadata, BASIC_BODY)

    assert ErrorCode.MANUAL_DERIVED_TAG in error_codes(tmp_path)


def test_derived_tags_have_deterministic_order_and_no_duplicates() -> None:
    card_metadata = metadata()
    card_metadata["tags"] = ["Memory", "Scenario", "Memory"]

    assert derived_tags(card_metadata) == [
        "A+::220-1201::1.1",
        "A+::220-1201::LaptopHardware",
        "Basic",
        "HighYield",
    ]
    assert final_tags(card_metadata) == [
        "A+::220-1201::1.1",
        "A+::220-1201::LaptopHardware",
        "Basic",
        "HighYield",
        "Memory",
        "Scenario",
    ]


def test_objective_13_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.3-B001")
    card_metadata.update(
        {
            "objective": "1.3",
            "objective_name": "Mobile Device Networks",
            "tags": ["Bluetooth", "Pairing"],
            "source": ["Professor Messer 220-1201 v1.70 p.4"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="1.3-mobile-device-networks",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::1.3",
        "A+::220-1201::Domain1-MobileDevices",
        "A+::220-1201::MobileDeviceNetworks",
        "Basic",
        "HighYield",
        "Bluetooth",
        "Pairing",
        "Source::Messer-v170",
    ]


def test_core2_objective_11_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata()
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective_name": "Operating System Types and Purposes",
            "tags": ["OS"],
            "source": ["Professor Messer 220-1202 v1.40 p.1"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.1-operating-system-types-and-purposes",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.1",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::OperatingSystemTypesandPurposes",
        "Basic",
        "HighYield",
        "OS",
        "Source::Messer-v140",
    ]


def test_core2_objective_12_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.2-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.2",
            "objective_name": "OS Installations and Upgrades",
            "tags": ["Installation"],
            "source": ["Professor Messer 220-1202 v1.40 p.3"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.2-os-installations-and-upgrades",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.2",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::OSInstallationsandUpgrades",
        "Basic",
        "HighYield",
        "Installation",
        "Source::Messer-v140",
    ]


def test_core2_objective_13_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.3-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.3",
            "objective_name": "Microsoft Windows Editions",
            "tags": ["Windows"],
            "source": ["Professor Messer 220-1202 v1.40 p.5"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.3-microsoft-windows-editions",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.3",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::MicrosoftWindowsEditions",
        "Basic",
        "HighYield",
        "Windows",
        "Source::Messer-v140",
    ]


def test_core2_objective_14_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.4-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.4",
            "objective_name": "Microsoft Windows Features and Tools",
            "tags": ["Windows"],
            "source": ["Professor Messer 220-1202 v1.40 p.7"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.4-microsoft-windows-features-and-tools",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.4",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::MicrosoftWindowsFeaturesandTools",
        "Basic",
        "HighYield",
        "Windows",
        "Source::Messer-v140",
    ]


def test_core2_objective_15_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.5-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.5",
            "objective_name": "Microsoft Command-line Tools",
            "tags": ["CLI"],
            "source": ["Professor Messer 220-1202 v1.40 p.9"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.5-microsoft-command-line-tools",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.5",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::MicrosoftCommandlineTools",
        "Basic",
        "HighYield",
        "CLI",
        "Source::Messer-v140",
    ]


def test_core2_objective_16_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.6-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.6",
            "objective_name": "Microsoft Windows Settings",
            "tags": ["WindowsSettings"],
            "source": ["Professor Messer 220-1202 v1.40 p.11"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.6-microsoft-windows-settings",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.6",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::MicrosoftWindowsSettings",
        "Basic",
        "HighYield",
        "WindowsSettings",
        "Source::Messer-v140",
    ]


def test_core2_objective_17_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.7-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.7",
            "objective_name": "Microsoft Windows Networking Features",
            "tags": ["WindowsNetworking"],
            "source": ["Professor Messer 220-1202 v1.40 p.13"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.7-microsoft-windows-networking-features",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.7",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::MicrosoftWindowsNetworkingFeatures",
        "Basic",
        "HighYield",
        "WindowsNetworking",
        "Source::Messer-v140",
    ]


def test_core2_objective_18_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.8-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.8",
            "objective_name": "macOS Features and Tools",
            "tags": ["macOS"],
            "source": ["Professor Messer 220-1202 v1.40 p.15"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.8-macos-features-and-tools",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.8",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::macOSFeaturesandTools",
        "Basic",
        "HighYield",
        "macOS",
        "Source::Messer-v140",
    ]


def test_core2_objective_19_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.9-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.9",
            "objective_name": "Linux Features and Tools",
            "tags": ["Linux"],
            "source": ["Professor Messer 220-1202 v1.40 p.18"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.9-linux-features-and-tools",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.9",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::LinuxFeaturesandTools",
        "Basic",
        "HighYield",
        "Linux",
        "Source::Messer-v140",
    ]


def test_core2_objective_110_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.10-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.10",
            "objective_name": "Application Installation Requirements",
            "tags": ["Applications"],
            "source": ["Professor Messer 220-1202 v1.40 p.22"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.10-application-installation-requirements",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.10",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::ApplicationInstallationRequirements",
        "Basic",
        "HighYield",
        "Applications",
        "Source::Messer-v140",
    ]


def test_core2_objective_111_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("1.11-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "1.11",
            "objective_name": "Cloud-Based Productivity Tools",
            "tags": ["CloudProductivity"],
            "source": ["Professor Messer 220-1202 v1.40 p.23"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="1.11-cloud-based-productivity-tools",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::1.11",
        "A+::220-1202::Domain1-OperatingSystems",
        "A+::220-1202::CloudBasedProductivityTools",
        "Basic",
        "HighYield",
        "CloudProductivity",
        "Source::Messer-v140",
    ]


def test_core2_objective_21_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.1-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.1",
            "objective_name": "Security Measures and Purposes",
            "tags": ["PhysicalSecurity"],
            "source": ["Professor Messer 220-1202 v1.40 p.24"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.1-security-measures-and-purposes",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.1",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::SecurityMeasuresandPurposes",
        "Basic",
        "HighYield",
        "PhysicalSecurity",
        "Source::Messer-v140",
    ]


def test_core2_objective_22_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.2-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.2",
            "objective_name": "Windows OS Security Settings",
            "tags": ["WindowsSecurity"],
            "source": ["Professor Messer 220-1202 v1.40 p.28"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.2-windows-os-security-settings",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.2",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::WindowsOSSecuritySettings",
        "Basic",
        "HighYield",
        "WindowsSecurity",
        "Source::Messer-v140",
    ]


def test_core2_objective_23_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.3-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.3",
            "objective_name": "Wireless Security Protocols and Authentication",
            "tags": ["WirelessSecurity"],
            "source": ["Professor Messer 220-1202 v1.40 p.31"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.3-wireless-security-protocols-and-authentication",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.3",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::WirelessSecurityProtocolsandAuthentication",
        "Basic",
        "HighYield",
        "WirelessSecurity",
        "Source::Messer-v140",
    ]


def test_core2_objective_24_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.4-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.4",
            "objective_name": "Malware Detection, Removal, and Prevention",
            "tags": ["Malware"],
            "source": ["Professor Messer 220-1202 v1.40 p.32"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.4-malware-detection-removal-and-prevention",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.4",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::MalwareDetectionRemovalandPrevention",
        "Basic",
        "HighYield",
        "Malware",
        "Source::Messer-v140",
    ]


def test_core2_objective_25_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.5-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.5",
            "objective_name": "Social Engineering, Threats, and Vulnerabilities",
            "tags": ["SocialEngineering"],
            "source": ["Professor Messer 220-1202 v1.40 p.35"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.5-social-engineering-threats-and-vulnerabilities",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.5",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::SocialEngineeringThreatsandVulnerabilities",
        "Basic",
        "HighYield",
        "SocialEngineering",
        "Source::Messer-v140",
    ]


def test_core2_objective_26_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.6-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.6",
            "objective_name": "SOHO Malware Removal Procedures",
            "tags": ["MalwareRemoval"],
            "source": ["Professor Messer 220-1202 v1.40 p.42"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.6-soho-malware-removal-procedures",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.6",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::SOHOMalwareRemovalProcedures",
        "Basic",
        "HighYield",
        "MalwareRemoval",
        "Source::Messer-v140",
    ]


def test_core2_objective_27_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.7-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.7",
            "objective_name": "Workstation Security and Hardening",
            "tags": ["Hardening"],
            "source": ["Professor Messer 220-1202 v1.40 p.43"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.7-workstation-security-and-hardening",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.7",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::WorkstationSecurityandHardening",
        "Basic",
        "HighYield",
        "Hardening",
        "Source::Messer-v140",
    ]


def test_core2_objective_28_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.8-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.8",
            "objective_name": "Mobile Device Security",
            "tags": ["MobileSecurity"],
            "source": ["Professor Messer 220-1202 v1.40 p.44"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.8-mobile-device-security",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.8",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::MobileDeviceSecurity",
        "Basic",
        "HighYield",
        "MobileSecurity",
        "Source::Messer-v140",
    ]


def test_core2_objective_29_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.9-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.9",
            "objective_name": "Data Destruction and Disposal",
            "tags": ["DataSanitization"],
            "source": ["Professor Messer 220-1202 v1.40 p.45"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.9-data-destruction-and-disposal",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.9",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::DataDestructionandDisposal",
        "Basic",
        "HighYield",
        "DataSanitization",
        "Source::Messer-v140",
    ]


def test_core2_objective_210_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.10-B001")
    card_metadata.update(
        {
            "exam": "220-1202",
            "objective": "2.10",
            "objective_name": "Securing a SOHO Network",
            "tags": ["RouterSecurity"],
            "source": ["Professor Messer 220-1202 v1.40 pp.46-47"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        exam_directory="220-1202",
        objective_directory="2.10-securing-a-soho-network",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1202::2.10",
        "A+::220-1202::Domain2-Security",
        "A+::220-1202::SecuringaSOHONetwork",
        "Basic",
        "HighYield",
        "RouterSecurity",
        "Source::Messer-v140",
    ]


def test_objective_21_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("2.1-C001", "cloze")
    card_metadata.update(
        {
            "objective": "2.1",
            "objective_name": "IP Addressing and Common Ports",
            "tags": ["TCP", "Ports"],
            "source": ["Professor Messer 220-1201 v1.70 p.6"],
            "high_yield": False,
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        CLOZE_BODY,
        objective_directory="2.1-ip-addressing-and-common-ports",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::2.1",
        "A+::220-1201::Domain2-Networking",
        "A+::220-1201::IPAddressingandCommonPorts",
        "Cloze",
        "TCP",
        "Ports",
        "Source::Messer-v170",
    ]


def test_objective_31_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("3.1-B001")
    card_metadata.update(
        {
            "objective": "3.1",
            "objective_name": "Display Types and Attributes",
            "tags": ["DisplayPanels", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.21"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="3.1-display-types-and-attributes",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::3.1",
        "A+::220-1201::Domain3-Hardware",
        "A+::220-1201::DisplayTypesandAttributes",
        "Basic",
        "HighYield",
        "DisplayPanels",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_32_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("3.2-B001")
    card_metadata.update(
        {
            "objective": "3.2",
            "objective_name": "Cable Types, Connectors, Features, and Purposes",
            "tags": ["CableTypes", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.23"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="3.2-cable-types-connectors-features-and-purposes",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::3.2",
        "A+::220-1201::Domain3-Hardware",
        "A+::220-1201::CableTypesConnectorsFeaturesandPurposes",
        "Basic",
        "HighYield",
        "CableTypes",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_33_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("3.3-B001")
    card_metadata.update(
        {
            "objective": "3.3",
            "objective_name": "RAM Characteristics",
            "tags": ["RAM", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.30"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="3.3-ram-characteristics",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::3.3",
        "A+::220-1201::Domain3-Hardware",
        "A+::220-1201::RAMCharacteristics",
        "Basic",
        "HighYield",
        "RAM",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_34_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("3.4-B001")
    card_metadata.update(
        {
            "objective": "3.4",
            "objective_name": "Storage Devices",
            "tags": ["Storage", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.32"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="3.4-storage-devices",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::3.4",
        "A+::220-1201::Domain3-Hardware",
        "A+::220-1201::StorageDevices",
        "Basic",
        "HighYield",
        "Storage",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_35_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("3.5-B001")
    card_metadata.update(
        {
            "objective": "3.5",
            "objective_name": "Motherboards, CPUs, and Add-on Cards",
            "tags": ["Motherboard", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.34"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="3.5-motherboards-cpus-and-add-on-cards",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::3.5",
        "A+::220-1201::Domain3-Hardware",
        "A+::220-1201::MotherboardsCPUsandAddonCards",
        "Basic",
        "HighYield",
        "Motherboard",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_36_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("3.6-B001")
    card_metadata.update(
        {
            "objective": "3.6",
            "objective_name": "Power Supplies",
            "tags": ["Power", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.40"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="3.6-power-supplies",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::3.6",
        "A+::220-1201::Domain3-Hardware",
        "A+::220-1201::PowerSupplies",
        "Basic",
        "HighYield",
        "Power",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_37_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("3.7-B001")
    card_metadata.update(
        {
            "objective": "3.7",
            "objective_name": "Multifunction Devices and Printers",
            "tags": ["Printer", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.41"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="3.7-multifunction-devices-and-printers",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::3.7",
        "A+::220-1201::Domain3-Hardware",
        "A+::220-1201::MultifunctionDevicesandPrinters",
        "Basic",
        "HighYield",
        "Printer",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_38_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("3.8-B001")
    card_metadata.update(
        {
            "objective": "3.8",
            "objective_name": "Printer Maintenance",
            "tags": ["Printer", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.43"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="3.8-printer-maintenance",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::3.8",
        "A+::220-1201::Domain3-Hardware",
        "A+::220-1201::PrinterMaintenance",
        "Basic",
        "HighYield",
        "Printer",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_41_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("4.1-B001")
    card_metadata.update(
        {
            "objective": "4.1",
            "objective_name": "Virtualization Concepts",
            "tags": ["Virtualization", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.46"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="4.1-virtualization-concepts",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::4.1",
        "A+::220-1201::Domain4-VirtualizationCloud",
        "A+::220-1201::VirtualizationConcepts",
        "Basic",
        "HighYield",
        "Virtualization",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_42_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("4.2-B001")
    card_metadata.update(
        {
            "objective": "4.2",
            "objective_name": "Cloud Computing Concepts",
            "tags": ["Cloud", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.47"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="4.2-cloud-computing-concepts",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::4.2",
        "A+::220-1201::Domain4-VirtualizationCloud",
        "A+::220-1201::CloudComputingConcepts",
        "Basic",
        "HighYield",
        "Cloud",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_51_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("5.1-B001")
    card_metadata.update(
        {
            "objective": "5.1",
            "objective_name": "Troubleshooting Hardware",
            "tags": ["POST", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.48"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="5.1-troubleshooting-hardware",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::5.1",
        "A+::220-1201::Domain5-Troubleshooting",
        "A+::220-1201::TroubleshootingHardware",
        "Basic",
        "HighYield",
        "POST",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_52_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("5.2-B001")
    card_metadata.update(
        {
            "objective": "5.2",
            "objective_name": "Troubleshooting Storage Devices",
            "tags": ["Storage", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.50"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="5.2-troubleshooting-storage-devices",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::5.2",
        "A+::220-1201::Domain5-Troubleshooting",
        "A+::220-1201::TroubleshootingStorageDevices",
        "Basic",
        "HighYield",
        "Storage",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_53_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("5.3-B001")
    card_metadata.update(
        {
            "objective": "5.3",
            "objective_name": "Troubleshooting Display Issues",
            "tags": ["Display", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.52"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="5.3-troubleshooting-display-issues",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::5.3",
        "A+::220-1201::Domain5-Troubleshooting",
        "A+::220-1201::TroubleshootingDisplayIssues",
        "Basic",
        "HighYield",
        "Display",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_54_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("5.4-B001")
    card_metadata.update(
        {
            "objective": "5.4",
            "objective_name": "Troubleshooting Mobile Devices",
            "tags": ["Mobile", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.53"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="5.4-troubleshooting-mobile-devices",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::5.4",
        "A+::220-1201::Domain5-Troubleshooting",
        "A+::220-1201::TroubleshootingMobileDevices",
        "Basic",
        "HighYield",
        "Mobile",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_55_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("5.5-B001")
    card_metadata.update(
        {
            "objective": "5.5",
            "objective_name": "Troubleshooting Networks",
            "tags": ["Network", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.55"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="5.5-troubleshooting-networks",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::5.5",
        "A+::220-1201::Domain5-Troubleshooting",
        "A+::220-1201::TroubleshootingNetworks",
        "Basic",
        "HighYield",
        "Network",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_objective_56_domain_and_source_validation_tags_are_generated(
    tmp_path: Path,
) -> None:
    card_metadata = metadata("5.6-B001")
    card_metadata.update(
        {
            "objective": "5.6",
            "objective_name": "Troubleshooting Printers",
            "tags": ["Printer", "Scenario"],
            "source": ["Professor Messer 220-1201 v1.70 p.56"],
        }
    )
    path = write_card(
        tmp_path,
        card_metadata,
        BASIC_BODY,
        objective_directory="5.6-troubleshooting-printers",
    )

    assert final_tags_for_card(parse_card(path)) == [
        "A+::220-1201::5.6",
        "A+::220-1201::Domain5-Troubleshooting",
        "A+::220-1201::TroubleshootingPrinters",
        "Basic",
        "HighYield",
        "Printer",
        "Scenario",
        "Source::Messer-v170",
    ]


def test_multiple_valid_clozes_are_allowed(tmp_path: Path) -> None:
    body = CLOZE_BODY.replace(
        "The answer is {{c1::here}}.",
        "Use {{c1::one}} and {{c2::two::a hint}}.",
    )
    write_card(tmp_path, metadata("1.1-C001", "cloze"), body)

    assert validate(tmp_path).valid


@pytest.mark.parametrize(
    "cloze",
    [
        "{{c1:answer}}",
        "{{c0::answer}}",
        "{{c::answer}}",
        "{{c1::}}",
        "{{c1::answer}",
        "{{c1::answer}}}",
        "{{{c1::answer}}",
    ],
)
def test_malformed_clozes_are_rejected(tmp_path: Path, cloze: str) -> None:
    body = CLOZE_BODY.replace("{{c1::here}}", f"{{{{c2::valid}}}} and {cloze}")
    write_card(tmp_path, metadata("1.1-C001", "cloze"), body)

    assert ErrorCode.INVALID_CLOZE in error_codes(tmp_path)


def test_missing_image_file_detection(tmp_path: Path) -> None:
    card_metadata = metadata("1.1-I001", "image")
    card_metadata["question_image"] = "assets/diagrams/220-1201/1.1/missing.svg"
    card_metadata["answer_image"] = "assets/diagrams/220-1201/1.1/also-missing.svg"
    write_card(tmp_path, card_metadata, IMAGE_BODY)

    assert error_codes(tmp_path).count(ErrorCode.MISSING_IMAGE) == 2


def test_image_path_traversal_is_rejected(tmp_path: Path) -> None:
    card_metadata = image_metadata(tmp_path)
    card_metadata["question_image"] = "assets/diagrams/../../outside.svg"
    write_card(tmp_path, card_metadata, IMAGE_BODY)

    assert ErrorCode.INVALID_IMAGE_PATH in error_codes(tmp_path)


def test_unsupported_image_extension_is_rejected(tmp_path: Path) -> None:
    unsupported = tmp_path / "assets" / "diagrams" / "220-1201" / "1.1" / "image.gif"
    unsupported.parent.mkdir(parents=True)
    unsupported.write_bytes(b"GIF89a")
    card_metadata = image_metadata(tmp_path)
    card_metadata["question_image"] = unsupported.relative_to(tmp_path).as_posix()
    write_card(tmp_path, card_metadata, IMAGE_BODY)

    assert ErrorCode.UNSUPPORTED_IMAGE_TYPE in error_codes(tmp_path)


def test_fenced_code_heading_is_not_a_section(tmp_path: Path) -> None:
    body = BASIC_BODY_WITH_HINT.replace(
        "The **answer**.",
        """The answer includes code:

```text
## This is code, not a section
value
```""",
    )
    path = write_card(tmp_path, metadata(), body)

    card = parse_card(path)

    assert validate(tmp_path).valid
    assert "## This is code" in card.sections["Answer"]


def test_markdown_to_html_supports_required_constructs() -> None:
    source = """\
Paragraph with **bold**, *italics*, `code`, and Unicode: café.

- one
- two

1. first
2. second

```shell
echo "hello"
```
"""

    rendered = markdown_to_html(source)

    assert "<strong>bold</strong>" in rendered
    assert "<em>italics</em>" in rendered
    assert "<code>code</code>" in rendered
    assert "<ul>" in rendered and "<ol>" in rendered
    assert '<code class="language-shell">' in rendered
    assert "café" in rendered


def test_exact_tsv_mapping_for_all_card_types(tmp_path: Path) -> None:
    write_card(tmp_path, metadata(), BASIC_BODY_WITH_HINT)
    write_card(tmp_path, metadata("1.1-C001", "cloze"), CLOZE_BODY)
    write_card(tmp_path, image_metadata(tmp_path), IMAGE_BODY)
    write_card(tmp_path, metadata("1.1-T001", "command"), COMMAND_BODY)

    files = generated_files(tmp_path)
    basic_columns, basic_rows, basic_comments = read_tsv(files["Basic.tsv"])
    cloze_columns, cloze_rows, _ = read_tsv(files["Cloze.tsv"])
    image_columns, image_rows, _ = read_tsv(files["Image.tsv"])
    command_columns, command_rows, command_comments = read_tsv(files["Command.tsv"])

    assert (
        basic_columns[0]
        == cloze_columns[0]
        == image_columns[0]
        == command_columns[0]
        == "Card ID"
    )
    assert basic_comments[:3] == ["#separator:Tab", "#html:true", "#tags column:10"]
    assert basic_rows[0] == [
        "1.1-B001",
        "<p>What is the answer?</p>",
        "<p>Think about the test fixture.</p>",
        "<p>The <strong>answer</strong>.</p>",
        "<p>Minimal test note.</p>",
        "easy",
        "basic",
        "220-1201 1.1 - Laptop Hardware",
        "Test fixture",
        "A+::220-1201::1.1 A+::220-1201::LaptopHardware "
        "Basic HighYield Memory Scenario",
    ]
    assert cloze_rows[0][0:4] == [
        "1.1-C001",
        "<p>The answer is {{c1::here}}.</p>",
        "<p>Minimal context.</p>",
        "<p>Minimal test note.</p>",
    ]
    assert cloze_rows[0][6] == "220-1201 1.1 - Laptop Hardware"
    assert image_rows[0][0:6] == [
        "1.1-I001",
        "<p>Identify the item.</p>",
        '<img src="1.1-I001-question.svg">',
        "<p>The item.</p>",
        '<img src="1.1-I001-answer.svg">',
        "<p>Minimal test note.</p>",
    ]
    assert image_rows[0][8] == "220-1201 1.1 - Laptop Hardware"
    assert command_comments[:3] == [
        "#separator:Tab",
        "#html:true",
        "#tags column:10",
    ]
    assert command_columns == [
        "Card ID",
        "Prompt",
        "Typed Answer",
        "Back",
        "Instructor Notes",
        "Difficulty",
        "Card Type",
        "Objective",
        "Source",
        "Tags",
    ]
    assert command_rows[0][0:8] == [
        "1.1-T001",
        "<p>Which command launches the tool?</p>",
        "tool.exe",
        "<p>The command launches the tool.</p>",
        "<p>Minimal test note.</p>",
        "easy",
        "command",
        "220-1201 1.1 - Laptop Hardware",
    ]


def test_basic_tsv_always_includes_empty_hint_column(tmp_path: Path) -> None:
    write_card(tmp_path, metadata(), BASIC_BODY)

    columns, rows, comments = read_tsv(generated_files(tmp_path)["Basic.tsv"])

    assert comments[:3] == ["#separator:Tab", "#html:true", "#tags column:10"]
    assert columns == [
        "Card ID",
        "Front",
        "Hint",
        "Back",
        "Instructor Notes",
        "Difficulty",
        "Card Type",
        "Objective",
        "Source",
        "Tags",
    ]
    assert rows[0][2] == ""
    assert rows[0][3] == "<p>The <strong>answer</strong>.</p>"


def test_cloze_image_and_command_tsv_schemas_do_not_include_hint(
    tmp_path: Path,
) -> None:
    write_card(tmp_path, metadata("1.1-C001", "cloze"), CLOZE_BODY)
    write_card(tmp_path, image_metadata(tmp_path), IMAGE_BODY)
    write_card(tmp_path, metadata("1.1-T001", "command"), COMMAND_BODY)

    files = generated_files(tmp_path)
    cloze_columns, _, cloze_comments = read_tsv(files["Cloze.tsv"])
    image_columns, _, image_comments = read_tsv(files["Image.tsv"])
    command_columns, _, command_comments = read_tsv(files["Command.tsv"])

    assert "Hint" not in cloze_columns
    assert "Hint" not in image_columns
    assert "Hint" not in command_columns
    assert cloze_comments[:3] == ["#separator:Tab", "#html:true", "#tags column:9"]
    assert image_comments[:3] == ["#separator:Tab", "#html:true", "#tags column:11"]
    assert command_comments[:3] == ["#separator:Tab", "#html:true", "#tags column:10"]


def test_media_folder_is_created_and_tsv_references_filenames_only(
    tmp_path: Path,
) -> None:
    write_card(tmp_path, image_metadata(tmp_path), IMAGE_BODY)

    files, media_paths = generated_outputs(tmp_path)
    _, image_rows, _ = read_tsv(files["Image.tsv"])

    assert sorted(path.name for path in media_paths) == [
        "1.1-I001-answer.svg",
        "1.1-I001-question.svg",
    ]
    assert all(
        path.parent
        == tmp_path / "output" / "media" / "220-1201" / "1.1-laptop-hardware"
        for path in media_paths
    )
    assert image_rows[0][2] == '<img src="1.1-I001-question.svg">'
    assert image_rows[0][4] == '<img src="1.1-I001-answer.svg">'
    assert "assets/" not in image_rows[0][2]
    assert "/" not in image_rows[0][2]


def test_generated_media_validation_rejects_missing_staged_media(
    tmp_path: Path,
) -> None:
    write_card(tmp_path, image_metadata(tmp_path), IMAGE_BODY)
    result = validate(tmp_path)
    assert result.valid
    output = tmp_path / "output" / "tsv"
    media = tmp_path / "output" / "media"

    generate_tsv(result.cards, tmp_path / "content", output)

    codes = [issue.code for issue in validate_generated_media(output, media)]
    assert ErrorCode.MISSING_IMAGE in codes


def test_build_cli_fails_when_image_file_is_missing(tmp_path: Path) -> None:
    card_metadata = metadata("1.1-I001", "image")
    card_metadata["question_image"] = "assets/diagrams/220-1201/1.1/missing.svg"
    card_metadata["answer_image"] = "assets/diagrams/220-1201/1.1/also-missing.svg"
    write_card(tmp_path, card_metadata, IMAGE_BODY)
    environment = os.environ.copy()
    environment["PYTHONPATH"] = os.pathsep.join(
        filter(None, [str(PROJECT_ROOT / "src"), environment.get("PYTHONPATH")])
    )

    completed = subprocess.run(
        [
            sys.executable,
            str(PROJECT_ROOT / "scripts" / "build.py"),
            "--repository-root",
            str(tmp_path),
        ],
        cwd=PROJECT_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 1
    assert ErrorCode.MISSING_IMAGE in completed.stdout


def test_media_generation_removes_stale_output(tmp_path: Path) -> None:
    write_card(tmp_path, image_metadata(tmp_path), IMAGE_BODY)
    stale = tmp_path / "output" / "media" / "old-exam" / "old-objective" / "old.svg"
    stale.parent.mkdir(parents=True)
    stale.write_text("<svg/>", encoding="utf-8")

    generated_outputs(tmp_path)

    assert not stale.exists()


def test_tsv_escapes_tabs_quotes_multiline_and_unicode(tmp_path: Path) -> None:
    card_metadata = metadata()
    card_metadata["source"] = ["Test\tfixture"]
    body = BASIC_BODY.replace(
        "What is the answer?",
        'A "quoted" question with\ta tab and café?',
    ).replace(
        "The **answer**.",
        """First paragraph.

Second paragraph.""",
    )
    write_card(tmp_path, card_metadata, body)

    _, rows, _ = read_tsv(generated_files(tmp_path)["Basic.tsv"])

    assert len(rows) == 1
    assert '"quoted"' in rows[0][1]
    assert "a tab" in rows[0][1]
    assert "café" in rows[0][1]
    assert "</p>\n<p>" in rows[0][3]
    assert rows[0][8] == "Test\tfixture"


def test_generation_removes_stale_output(tmp_path: Path) -> None:
    write_card(tmp_path, metadata(), BASIC_BODY)
    stale = tmp_path / "output" / "tsv" / "old-exam" / "old-objective" / "Basic.tsv"
    stale.parent.mkdir(parents=True)
    stale.write_text("stale", encoding="utf-8")

    generated_files(tmp_path)

    assert not stale.exists()


def test_generation_failure_preserves_previous_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    write_card(tmp_path, metadata(), BASIC_BODY)
    result = validate(tmp_path)
    output = tmp_path / "output" / "tsv"
    previous = output / "previous.tsv"
    previous.parent.mkdir(parents=True)
    previous.write_text("previous", encoding="utf-8")

    def fail_write(*_args: object, **_kwargs: object) -> None:
        raise OSError("simulated write failure")

    monkeypatch.setattr(pipeline, "_write_tsv", fail_write)

    with pytest.raises(OSError, match="simulated write failure"):
        generate_tsv(result.cards, tmp_path / "content", output)
    assert previous.read_text(encoding="utf-8") == "previous"


def test_generation_is_reproducible(tmp_path: Path) -> None:
    write_card(tmp_path, metadata(), BASIC_BODY)

    first = generated_files(tmp_path)["Basic.tsv"].read_bytes()
    second = generated_files(tmp_path)["Basic.tsv"].read_bytes()

    assert first == second


def test_validation_cli_fails_with_coded_error(tmp_path: Path) -> None:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = os.pathsep.join(
        filter(None, [str(PROJECT_ROOT / "src"), environment.get("PYTHONPATH")])
    )

    completed = subprocess.run(
        [
            sys.executable,
            str(PROJECT_ROOT / "scripts" / "validate.py"),
            "--repository-root",
            str(tmp_path),
        ],
        cwd=PROJECT_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 1
    assert ErrorCode.NO_CARDS in completed.stdout
