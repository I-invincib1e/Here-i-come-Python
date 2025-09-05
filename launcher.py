import subprocess
import sys
from pathlib import Path


PROJECTS = [
    # Level 1 - Simple Starters
    ("1", "level1/guess_number", "Guess the Number"),
    ("2", "level1/calculator_cli", "Calculator CLI"),
    ("3", "level1/todo_cli", "Todo CLI"),
    ("4", "level1/stopwatch_cli", "Stopwatch CLI"),
    ("5", "level1/rock_paper_scissors", "Rock, Paper, Scissors"),
    # Level 2 - Uplifted Mid-Level
    ("6", "level2/tictactoe_ai", "Tic Tac Toe (AI)"),
    ("7", "level2/expense_tracker", "Expense Tracker"),
    ("8", "level2/file_organizer", "File Organizer"),
    ("9", "level2/md_notes", "Markdown Notes"),
    ("10", "level2/quiz_game", "Quiz Game"),
]


def main() -> None:
    print("Python Practice Projects")
    print("\nLevel 1 - Simple Starters:")
    for key, folder, title in PROJECTS[:5]:
        print(f"  {key}. {title}")
    print("\nLevel 2 - Uplifted Mid-Level:")
    for key, folder, title in PROJECTS[5:]:
        print(f"  {key}. {title}")
    print("\nq. Quit\n")

    choice = input("Select a project: ").strip().lower()
    if choice in {"q", "quit", "exit"}:
        return

    for key, folder, _ in PROJECTS:
        if choice == key:
            script = Path(folder) / "main.py"
            if not script.exists():
                print("Project script not found.")
                return
            subprocess.run([sys.executable, str(script)])
            return
    print("Invalid selection.")


if __name__ == "__main__":
    main()


