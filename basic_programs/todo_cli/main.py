from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

from shared.cli_utils import create_repl_loop
from shared.path_utils import get_project_dir


PROJECT_DIR = get_project_dir(Path(__file__))
DATA_FILE = PROJECT_DIR / "todos.json"


@dataclass
class Todo:
    id: int
    title: str
    done: bool = False


def load_todos() -> List[Todo]:
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return [Todo(**item) for item in data]
    except (OSError, json.JSONDecodeError, TypeError, KeyError):
        return []


def save_todos(todos: List[Todo]) -> None:
    DATA_FILE.write_text(
        json.dumps([asdict(t) for t in todos], indent=2), encoding="utf-8"
    )


def next_id(todos: List[Todo]) -> int:
    return (max((t.id for t in todos), default=0) + 1)


def add(title: str) -> None:
    todos = load_todos()
    todos.append(Todo(id=next_id(todos), title=title))
    save_todos(todos)
    print("Added.")


def list_todos() -> None:
    todos = load_todos()
    if not todos:
        print("No todos yet.")
        return
    for t in todos:
        status = "[x]" if t.done else "[ ]"
        print(f"{t.id:3} {status} {t.title}")


def complete(todo_id: int) -> None:
    todos = load_todos()
    for t in todos:
        if t.id == todo_id:
            t.done = True
            save_todos(todos)
            print("Completed.")
            return
    print("Todo not found.")


def delete(todo_id: int) -> None:
    todos = load_todos()
    new_todos = [t for t in todos if t.id != todo_id]
    if len(new_todos) == len(todos):
        print("Todo not found.")
        return
    save_todos(new_todos)
    print("Deleted.")


def print_help() -> None:
    print("Todo CLI")
    print("Commands:")
    print("  add <title>       Add a new todo")
    print("  list              List todos")
    print("  done <id>         Mark todo as completed")
    print("  del <id>          Delete a todo")
    print("  help              Show this help")


def process_command(line: str) -> None:
    parts = line.strip().split()
    if not parts:
        return
    cmd, *args = parts
    if cmd == "add":
        if not args:
            print("Usage: add <title>")
            return
        add(" ".join(args))
    elif cmd == "list":
        list_todos()
    elif cmd in {"done", "del"}:
        if len(args) != 1 or not args[0].isdigit():
            print(f"Usage: {cmd} <id>")
            return
        todo_id = int(args[0])
        if cmd == "done":
            complete(todo_id)
        else:
            delete(todo_id)
    elif cmd in {"help", "-h", "--help"}:
        print_help()
    else:
        print("Unknown command. Type 'help' for usage.")


def main(_argv: List[str]) -> None:
    print("Todo CLI (type 'help' or 'q' to quit)\n")
    create_repl_loop(process_command, "", "> ")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])


