from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "install_anki_media.py"
SPEC = importlib.util.spec_from_file_location("install_anki_media", SCRIPT_PATH)
assert SPEC is not None
install_anki_media = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["install_anki_media"] = install_anki_media
SPEC.loader.exec_module(install_anki_media)


def write_media(path: Path, content: str = "<svg/>") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_dry_run_does_not_copy(tmp_path: Path) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "collection.media"
    write_media(source / "1.1-I001-question.svg")
    destination.mkdir()

    result = install_anki_media.install_media(source, destination, dry_run=True)

    assert result.ok
    assert result.copied == 1
    assert not (destination / "1.1-I001-question.svg").exists()


def test_copies_supported_files(tmp_path: Path) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "collection.media"
    write_media(source / "1.1-I001-question.svg", "<svg>source</svg>")
    destination.mkdir()

    result = install_anki_media.install_media(source, destination)

    assert result.ok
    assert result.copied == 1
    assert (destination / "1.1-I001-question.svg").read_text(encoding="utf-8") == (
        "<svg>source</svg>"
    )


def test_skips_identical_existing_files(tmp_path: Path) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "collection.media"
    write_media(source / "1.1-I001-question.svg", "<svg>same</svg>")
    write_media(destination / "1.1-I001-question.svg", "<svg>same</svg>")

    result = install_anki_media.install_media(source, destination)

    assert result.ok
    assert result.copied == 0
    assert result.skipped == 1


def test_fails_on_differing_existing_file_without_overwrite(tmp_path: Path) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "collection.media"
    write_media(source / "1.1-I001-question.svg", "<svg>source</svg>")
    write_media(destination / "1.1-I001-question.svg", "<svg>destination</svg>")

    result = install_anki_media.install_media(source, destination)

    assert not result.ok
    assert result.failed == 1
    assert (destination / "1.1-I001-question.svg").read_text(encoding="utf-8") == (
        "<svg>destination</svg>"
    )


def test_overwrites_with_overwrite(tmp_path: Path) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "collection.media"
    write_media(source / "1.1-I001-question.svg", "<svg>source</svg>")
    write_media(destination / "1.1-I001-question.svg", "<svg>destination</svg>")

    result = install_anki_media.install_media(source, destination, overwrite=True)

    assert result.ok
    assert result.copied == 1
    assert (destination / "1.1-I001-question.svg").read_text(encoding="utf-8") == (
        "<svg>source</svg>"
    )


def test_rejects_missing_source_directory(tmp_path: Path) -> None:
    destination = tmp_path / "collection.media"
    destination.mkdir()

    result = install_anki_media.install_media(tmp_path / "missing", destination)

    assert not result.ok
    assert result.failed == 1
    assert "Source media directory does not exist" in result.messages[0]


def test_rejects_missing_destination_directory(tmp_path: Path) -> None:
    source = tmp_path / "source"
    write_media(source / "1.1-I001-question.svg")

    result = install_anki_media.install_media(source, tmp_path / "missing")

    assert not result.ok
    assert result.failed == 1
    assert "Destination collection.media directory does not exist" in result.messages[0]


def test_rejects_unsupported_file_types(tmp_path: Path) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "collection.media"
    write_media(source / "1.1-I001-question.svg")
    write_media(source / "notes.txt", "not media")
    destination.mkdir()

    result = install_anki_media.install_media(source, destination)

    assert not result.ok
    assert result.copied == 1
    assert result.failed == 1
    assert "Unsupported media file type: notes.txt" in result.messages


def test_destination_uses_explicit_media_dir_without_profile(tmp_path: Path) -> None:
    args = install_anki_media.parse_args(
        ["--media-dir", str(tmp_path), "--objective", "1.1-laptop-hardware"]
    )

    assert install_anki_media.destination_media_dir(args) == tmp_path


def test_profile_required_without_explicit_media_dir(tmp_path: Path) -> None:
    args = install_anki_media.parse_args(
        ["--anki-base", str(tmp_path), "--objective", "1.1-laptop-hardware"]
    )

    try:
        install_anki_media.destination_media_dir(args)
    except ValueError as error:
        assert "--profile is required" in str(error)
    else:
        raise AssertionError("expected missing profile to fail")
