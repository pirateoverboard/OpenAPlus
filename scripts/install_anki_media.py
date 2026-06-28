"""Install generated OpenAPlus media into a local Anki collection.media folder."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from dataclasses import dataclass, field
from pathlib import Path

SUPPORTED_MEDIA_EXTENSIONS = frozenset({".svg", ".png", ".jpg", ".jpeg", ".webp"})
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class InstallResult:
    """Summary of one media installation attempt."""

    copied: int = 0
    skipped: int = 0
    failed: int = 0
    messages: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.failed == 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", help='Anki profile name, for example "User 1"')
    parser.add_argument("--exam", default="220-1201")
    parser.add_argument("--objective", required=True)
    parser.add_argument(
        "--anki-base",
        type=Path,
        default=Path("~/.local/share/Anki2"),
        help="Base Anki2 directory; defaults to ~/.local/share/Anki2",
    )
    parser.add_argument(
        "--media-dir",
        type=Path,
        help="Explicit destination collection.media path",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args(argv)


def source_media_dir(repository_root: Path, exam: str, objective: str) -> Path:
    """Return the generated source media directory for one objective."""

    return repository_root / "output" / "media" / exam / objective


def destination_media_dir(args: argparse.Namespace) -> Path:
    """Return the requested Anki collection.media destination."""

    if args.media_dir is not None:
        return args.media_dir.expanduser()
    if not args.profile:
        raise ValueError("--profile is required unless --media-dir is provided")
    return args.anki_base.expanduser() / args.profile / "collection.media"


def install_media(
    source_dir: Path,
    destination_dir: Path,
    *,
    dry_run: bool = False,
    overwrite: bool = False,
) -> InstallResult:
    """Copy media files from one generated objective into Anki media."""

    result = InstallResult()
    if not source_dir.is_dir():
        result.failed += 1
        result.messages.append(f"Source media directory does not exist: {source_dir}")
        return result
    if not destination_dir.is_dir():
        result.failed += 1
        result.messages.append(
            f"Destination collection.media directory does not exist: {destination_dir}"
        )
        return result

    for source in sorted(source_dir.iterdir()):
        if not source.is_file():
            result.failed += 1
            result.messages.append(f"Unsupported media entry is not a file: {source}")
            continue
        if source.suffix.lower() not in SUPPORTED_MEDIA_EXTENSIONS:
            result.failed += 1
            result.messages.append(f"Unsupported media file type: {source.name}")
            continue

        destination = destination_dir / source.name
        destination_exists = destination.exists()
        if destination_exists:
            if not destination.is_file():
                result.failed += 1
                result.messages.append(
                    f"Destination exists but is not a file: {destination}"
                )
                continue
            if filecmp.cmp(source, destination, shallow=False):
                result.skipped += 1
                result.messages.append(f"Skipped identical file: {source.name}")
                continue
            if not overwrite:
                result.failed += 1
                result.messages.append(
                    f"Destination differs; use --overwrite to replace: {source.name}"
                )
                continue

        if dry_run:
            result.copied += 1
            action = "Would overwrite" if destination_exists else "Would copy"
            result.messages.append(f"{action}: {source.name}")
            continue

        shutil.copy2(source, destination)
        result.copied += 1
        action = "Overwrote" if destination_exists else "Copied"
        result.messages.append(f"{action}: {source.name}")

    return result


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        destination = destination_media_dir(args)
    except ValueError as error:
        print(f"ERROR: {error}")
        return 2

    source = source_media_dir(REPOSITORY_ROOT, args.exam, args.objective)
    result = install_media(
        source,
        destination,
        dry_run=args.dry_run,
        overwrite=args.overwrite,
    )
    for message in result.messages:
        print(message)
    print(
        f"Media install complete: copied={result.copied} "
        f"skipped={result.skipped} failed={result.failed}"
    )
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
