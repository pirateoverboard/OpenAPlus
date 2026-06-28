"""Generate Anki-ready TSV files from validated OpenAPlus cards."""

import argparse
from pathlib import Path

from openaplus.content_pipeline import format_issue, generate_tsv, validate_cards

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
    result = validate_cards(content_root, repository_root)
    if not result.valid:
        for error in result.errors:
            print(f"ERROR: {format_issue(error, repository_root)}")
        print("TSV generation stopped because validation failed.")
        return 1

    print("Generating TSV files...")
    for path in generate_tsv(result.cards, content_root, output_root):
        print(f"Generated {path.relative_to(output_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
