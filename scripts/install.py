#!/usr/bin/env python3
"""Install the skill; updates require --update and preserve the previous folder."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import stat
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "im-novelist"
PACKAGE = ("SKILL.md", "references", "agents", "LICENSE", "scripts/count_text.py")
LOCATIONS = {
    "claude": Path(".claude/skills"),
    "gemini": Path(".gemini/skills"),
    "codex": Path(".agents/skills"),
    "antigravity": Path(".gemini/config/skills"),
    "antigravity-cli": Path(".gemini/antigravity-cli/skills"),
}
PROJECT_LOCATIONS = {**LOCATIONS, "antigravity": Path(".agents/skills"), "antigravity-cli": Path(".agents/skills")}


def is_link(path: Path) -> bool:
    """Reject symbolic links and Windows junctions without following their targets."""
    if path.is_symlink():
        return True
    try:
        return getattr(path.lstat(), "st_reparse_tag", None) == getattr(stat, "IO_REPARSE_TAG_MOUNT_POINT", 0xA0000003)
    except FileNotFoundError:
        return False


def has_skill_name(data: bytes, name: str) -> bool:
    """Accept UTF-8 BOM and LF/CRLF checkouts while retaining the exact skill identity."""
    try:
        return data.decode("utf-8-sig").splitlines()[:2] == ["---", f"name: {name}"]
    except UnicodeDecodeError:
        return False


def destination_for(tool: str, *, project: Path | None = None, home: Path | None = None) -> Path:
    base = project.expanduser().resolve() if project is not None else (home or Path.home())
    locations = PROJECT_LOCATIONS if project is not None else LOCATIONS
    return base / locations[tool] / NAME


def checked_files(root: Path) -> list[Path]:
    """Inspect directory entries before descending into them (also for Windows junctions)."""
    result = []
    pending = [root]
    while pending:
        path = pending.pop()
        if is_link(path):
            raise ValueError(f"Refusing a link or junction: {path}")
        if path.is_dir():
            pending.extend(sorted(path.iterdir()))
        elif path.is_file():
            result.append(path)
    return result


def package_files(source: Path) -> dict[str, bytes]:
    result: dict[str, bytes] = {}
    if is_link(source):
        raise ValueError("Package root cannot be a link or junction")
    for entry in PACKAGE:
        path = source / entry
        if is_link(path):
            raise ValueError(f"Package contains a link or junction: {entry}")
        if not path.exists():
            raise ValueError(f"Missing package entry: {entry}")
        candidates = checked_files(path)
        for candidate in candidates:
            if is_link(candidate):
                raise ValueError(f"Package contains a symlink: {candidate.name}")
            if candidate.is_file():
                result[candidate.relative_to(source).as_posix()] = candidate.read_bytes()
    if not has_skill_name(result.get("SKILL.md", b""), NAME):
        raise ValueError("Unexpected skill name or missing frontmatter")
    return result


def existing_files(target: Path) -> dict[str, bytes]:
    result: dict[str, bytes] = {}
    for path in checked_files(target):
        if is_link(path):
            raise FileExistsError(f"Refusing to replace symlink inside {target}")
        if path.is_file():
            result[path.relative_to(target).as_posix()] = path.read_bytes()
    return result


def install(source: Path, target: Path, *, dry_run: bool = False, update: bool = False) -> str:
    files = package_files(source)
    if is_link(target):
        raise FileExistsError(f"Refusing to replace symlink: {target}")
    updating = target.exists()
    if updating:
        if not target.is_dir():
            raise FileExistsError(f"Destination is not a directory: {target}")
        previous = existing_files(target)
        if previous == files:
            return f"Already current: {target}"
        if not update:
            raise FileExistsError(
                f"Existing destination differs: {target}. "
                "Use --update to keep a backup and replace it, or choose --destination. "
                "Nothing was overwritten."
            )
        if not has_skill_name(previous.get("SKILL.md", b""), NAME):
            raise ValueError(f"Existing destination is not an im-novelist skill: {target}")
    if dry_run:
        verb = "update with backup" if updating else "install"
        return f"Would {verb} {len(files)} files: {target}"
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".im-novelist-stage-", dir=target.parent))
    try:
        for relative, data in files.items():
            destination = stage / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
        if updating:
            # Preserve all existing files, including user additions, before replacing.
            if is_link(target) or not target.is_dir() or existing_files(target) != previous:
                raise FileExistsError(f"Destination changed during installation: {target}")
            backup = Path(tempfile.mkdtemp(prefix=".im-novelist-backup-", dir=target.parent))
            backup.rmdir()
            target.rename(backup)
            try:
                if os.path.lexists(target):
                    raise FileExistsError(f"Destination appeared during installation: {target}")
                stage.rename(target)
            except BaseException:
                if not os.path.lexists(target):
                    backup.rename(target)
                raise
            return f"Updated: {target}\nBackup: {backup}"
        # Refuse a destination that appeared during copying, including broken links.
        if os.path.lexists(target):
            raise FileExistsError(f"Destination appeared during installation: {target}")
        stage.rename(target)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return f"Installed: {target}"


def migrate_legacy(source: Path, target: Path, legacy: Path, *, dry_run: bool = False) -> str:
    """Move an explicitly selected im-poetry install into a backup, then install this name."""
    files = package_files(source)
    if os.path.lexists(target):
        raise FileExistsError(f"New destination already exists; migration stopped: {target}")
    if is_link(legacy) or not legacy.is_dir():
        raise ValueError(f"Legacy destination must be a real skill directory: {legacy}")
    previous = existing_files(legacy)
    if not has_skill_name(previous.get("SKILL.md", b""), "im-poetry"):
        raise ValueError(f"Legacy destination is not an im-poetry skill: {legacy}")
    if target.absolute().is_relative_to(legacy.absolute()):
        raise ValueError("New destination cannot be inside the legacy skill")
    if dry_run:
        return f"Would migrate with backup {len(files)} files: {legacy} -> {target}"
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".im-novelist-migrate-", dir=target.parent))
    try:
        staged_skill = stage / "skill"
        install(source, staged_skill)
        if is_link(legacy) or not legacy.is_dir() or existing_files(legacy) != previous:
            raise FileExistsError(f"Legacy destination changed during migration: {legacy}")
        backup = Path(tempfile.mkdtemp(prefix=".im-poetry-backup-", dir=legacy.parent))
        backup.rmdir()
        legacy.rename(backup)
        try:
            if os.path.lexists(target):
                raise FileExistsError(f"Destination appeared during migration: {target}")
            staged_skill.rename(target)
        except BaseException:
            if not os.path.lexists(legacy):
                backup.rename(legacy)
            raise
        return f"Migrated: {target}\nBackup: {backup}"
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--target", choices=sorted(LOCATIONS))
    choice.add_argument("--destination", type=Path, help="Exact destination skill directory")
    parser.add_argument("--project", type=Path, help="Project root; default is the user home")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--update", action="store_true", help="Back up and replace an existing im-novelist skill")
    parser.add_argument("--migrate-from", type=Path, help="Back up a legacy im-poetry skill and install as im-novelist")
    args = parser.parse_args()
    if args.destination and args.project:
        parser.error("--project cannot be combined with --destination")
    if args.update and args.migrate_from:
        parser.error("--update cannot be combined with --migrate-from")
    target = (
        args.destination.expanduser().absolute()
        if args.destination
        else destination_for(args.target, project=args.project)
    )
    try:
        if args.migrate_from:
            print(migrate_legacy(ROOT, target, args.migrate_from.expanduser().absolute(), dry_run=args.dry_run))
        else:
            print(install(ROOT, target, dry_run=args.dry_run, update=args.update))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Installation stopped: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
