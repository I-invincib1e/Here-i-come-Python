from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple


DEFAULT_CONFIG = {
    "images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "documents": [".pdf", ".docx", ".txt", ".md"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "audio": [".mp3", ".wav", ".flac"],
    "videos": [".mp4", ".mkv", ".mov", ".avi"],
}


def load_config(config_path: Path | None) -> Dict[str, List[str]]:
    if config_path and config_path.exists():
        try:
            return json.loads(config_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return DEFAULT_CONFIG


def categorize(file: Path, rules: Dict[str, List[str]]) -> str:
    ext = file.suffix.lower()
    for category, extensions in rules.items():
        if ext in extensions:
            return category
    return "others"


def plan_moves(src: Path, dest: Path, rules: Dict[str, List[str]]) -> List[Tuple[Path, Path]]:
    moves: List[Tuple[Path, Path]] = []
    for item in src.iterdir():
        if item.is_dir():
            continue
        category = categorize(item, rules)
        target_dir = dest / category
        target_dir.mkdir(parents=True, exist_ok=True)
        moves.append((item, target_dir / item.name))
    return moves


def execute_moves(moves: List[Tuple[Path, Path]], dry_run: bool) -> None:
    for src, dst in moves:
        if dry_run:
            print(f"DRY-RUN: {src} -> {dst}")
        else:
            shutil.move(str(src), str(dst))
            print(f"Moved: {src.name} -> {dst}")


VERSION = "1.0.0"


def help_text() -> None:
    print("File Organizer")
    print("Usage:")
    print("  organize <source_dir> <dest_dir> [--config path] [--dry-run]")
    print("  --help | -h")
    print(f"  --version  (v{VERSION})")


def main(argv: List[str]) -> None:
    if not argv or argv[0] in {"help", "-h", "--help"}:
        help_text()
        return
    if argv[0] in {"--version", "-V"}:
        print(VERSION)
        return
    if argv[0] != "organize" or len(argv) < 3:
        help_text()
        return

    src = Path(argv[1]).expanduser().resolve()
    dest = Path(argv[2]).expanduser().resolve()
    dry_run = "--dry-run" in argv
    config: Path | None = None
    if "--config" in argv:
        try:
            idx = argv.index("--config")
            config = Path(argv[idx + 1])
        except Exception:
            print("Invalid --config usage")
            return

    if not src.exists() or not src.is_dir():
        print("Source directory not found.")
        return
    dest.mkdir(parents=True, exist_ok=True)

    rules = load_config(config)
    moves = plan_moves(src, dest, rules)
    if not moves:
        print("No files to organize.")
        return
    execute_moves(moves, dry_run)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])


