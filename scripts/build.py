"""Validate source cards and generate all OpenAPlus outputs."""

import argparse
from pathlib import Path

from openaplus.content_pipeline import (
    build_media,
    format_issue,
    generate_tsv,
    validate_cards,
    validate_generated_media,
)

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=REPOSITORY_ROOT)
    parser.add_argument("--content-root", type=Path)
    parser.add_argument("--output-root", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repository_root = args.repository_root.resolve()
    content_root = (args.content_root or repository_root / "content").resolve()
    output_root = (args.output_root or repository_root / "output" / "tsv").resolve()
    media_root = repository_root / "output" / "media"
    print("Validating cards...")
    result = validate_cards(content_root, repository_root)
    for warning in result.warnings:
        print(f"WARNING: {format_issue(warning, repository_root)}")
    for error in result.errors:
        print(f"ERROR: {format_issue(error, repository_root)}")
    if not result.valid:
        print(f"Validation failed with {len(result.errors)} error(s).")
        return 1
    print("Validation passed.")

    print("Generating TSV files...")
    for path in generate_tsv(result.cards, content_root, output_root):
        print(f"Generated {path.name}")

    print("Building media files...")
    for path in build_media(result.cards, content_root, repository_root, media_root):
        print(f"Staged {path.relative_to(media_root)}")

    print("Rewriting TSV files with staged media references...")
    for path in generate_tsv(result.cards, content_root, output_root):
        print(f"Rewrote {path.name}")

    print("Validating generated media references...")
    media_errors = validate_generated_media(output_root, media_root)
    for error in media_errors:
        print(f"ERROR: {format_issue(error, repository_root)}")
    if media_errors:
        print(f"Generated media validation failed with {len(media_errors)} error(s).")
        return 1

    print("Build complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
