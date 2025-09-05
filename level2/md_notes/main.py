from __future__ import annotations

import re
from pathlib import Path
from typing import List


NOTES_DIR = Path(__file__).with_name("notes")
NOTES_DIR.mkdir(exist_ok=True)


def list_notes() -> None:
    files = sorted(NOTES_DIR.glob("*.md"))
    if not files:
        print("No notes found.")
        return
    for f in files:
        print(f.name)


def create_note(title: str, content: str) -> None:
    safe_name = re.sub(r"[^a-zA-Z0-9_-]+", "_", title).strip("_") or "note"
    path = NOTES_DIR / f"{safe_name}.md"
    if path.exists():
        print("Note already exists.")
        return
    path.write_text(f"# {title}\n\n{content}\n", encoding="utf-8")
    print(f"Created {path.name}")


def view_note(name: str) -> None:
    path = NOTES_DIR / name
    if not path.exists():
        print("Note not found.")
        return
    print(path.read_text(encoding="utf-8"))


def render_note(name: str) -> None:
    path = NOTES_DIR / name
    if not path.exists():
        print("Note not found.")
        return
    text = path.read_text(encoding="utf-8")
    html = markdown_to_html(text)
    out = path.with_suffix(".html")
    out.write_text(html, encoding="utf-8")
    print(f"Rendered to {out.name}")


def markdown_to_html(text: str) -> str:
    lines = text.splitlines()
    html_lines: List[str] = [
        "<html><head><meta charset='utf-8'><title>Note</title></head><body>"
    ]
    for line in lines:
        if line.startswith("# "):
            html_lines.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith("### "):
            html_lines.append(f"<h3>{line[4:].strip()}</h3>")
        elif line.strip() == "":
            html_lines.append("<br/>")
        else:
            line = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line)
            line = re.sub(r"\*(.+?)\*", r"<em>\1</em>", line)
            html_lines.append(f"<p>{line}</p>")
    html_lines.append("</body></html>")
    return "\n".join(html_lines)


def help_text() -> None:
    print("Markdown Notes")
    print("Commands:")
    print("  list")
    print("  new <title> <content...>")
    print("  view <filename.md>")
    print("  render <filename.md>")


def main(argv: List[str]) -> None:
    if not argv or argv[0] in {"help", "-h", "--help"}:
        help_text()
        return
    cmd = argv[0]
    if cmd == "list":
        list_notes()
    elif cmd == "new":
        if len(argv) < 3:
            print("Usage: new <title> <content...>")
            return
        create_note(argv[1], " ".join(argv[2:]))
    elif cmd == "view":
        if len(argv) != 2:
            print("Usage: view <filename.md>")
            return
        view_note(argv[1])
    elif cmd == "render":
        if len(argv) != 2:
            print("Usage: render <filename.md>")
            return
        render_note(argv[1])
    else:
        print("Unknown command. Type 'help' for usage.")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])


