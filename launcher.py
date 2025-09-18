import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


def discover_projects(base_dir: Path) -> List[Tuple[str, str, str]]:
    """Discover projects under base_dir that contain a main.py.

    Returns list of (key, folder, title) sorted by folder name.
    """
    entries: List[Tuple[str, str, str]] = []
    projects = []
    if not base_dir.exists():
        return entries

    for sub in sorted(base_dir.iterdir()):
        if not sub.is_dir():
            continue
        script = sub / "main.py"
        if script.exists():
            title = sub.name.replace("_", " ").title()
            projects.append((str(sub), title))

    for idx, (folder, title) in enumerate(projects, start=1):
        entries.append((str(idx), folder, title))

    return entries


def main() -> None:
    base = Path("basic_programs")
    projects = discover_projects(base)

    if not projects:
        print("No projects found under 'basic_programs/'.")
        return

    print("Python Practice Projects\n")
    for key, _folder, title in projects:
        print(f"  {key}. {title}")
    print("\nq. Quit\n")

    choice = input("Select a project: ").strip().lower()
    if choice in {"q", "quit", "exit"}:
        return

    for key, folder, _ in projects:
        if choice == key:
            script = Path(folder) / "main.py"
            if not script.exists():
                print("Project script not found.")
                return
            subprocess.run([sys.executable, str(script)], check=False)
            return
    print("Invalid selection.")


if __name__ == "__main__":
    main()


