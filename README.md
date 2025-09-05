# Python Practice Projects (Beginner to Mid-Level)

![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Beginner Friendly](https://img.shields.io/badge/beginner-friendly-blue)

A single repository of 10 hands-on Python projects designed for beginners to learn by building. Projects are grouped into two levels:

- Level 1: Simple starters (5 projects)
- Level 2: Uplifted mid-level (5 projects)

All projects are standard-library only (no external dependencies) and runnable from the command line.

## Prerequisites

- Python 3.8+ installed
- Windows PowerShell or a Unix shell (macOS/Linux)

## How to Run

From the repository root:

- Windows PowerShell: `python .\\level1\\<project_folder>\\main.py`
- macOS/Linux: `python3 ./level1/<project_folder>/main.py`

Or use the interactive launcher:

- Windows PowerShell: `python .\\launcher.py`
- macOS/Linux: `python3 ./launcher.py`

## Projects

### Level 1 – Simple Starters (`level1/`)

1. **guess_number** – Guess the number between 1–100 in 10 attempts
2. **calculator_cli** – REPL calculator supporting + - * / ^
3. **todo_cli** – JSON-persistent todo list with add/list/done/del
4. **stopwatch_cli** – Interactive stopwatch with laps
5. **rock_paper_scissors** – Play against the computer

### Level 2 – Uplifted Mid-Level (`level2/`)

6. **tictactoe_ai** – Tic Tac Toe vs minimax AI (alpha–beta)
7. **expense_tracker** – CSV-based expense tracker and monthly reports
8. **file_organizer** – Organize files by type; JSON config; --dry-run
9. **md_notes** – Markdown notes manager with basic HTML renderer
10. **quiz_game** – Multiple-choice quiz with JSON questions and highscores

## Start Here

- Read the short overview: `docs/overview.md`
- Follow the step-by-step plan: `docs/LEARNING_PATH.md`
- Want to contribute? See `CONTRIBUTING.md` and `docs/CONTRIBUTING_GUIDE.md`
- Looking for tasks? Check `docs/GOOD_FIRST_ISSUES.md` for ready-to-pick items.
- **Maintainers**: Use `scripts/create_issues.ps1|.sh` with `scripts/issues_config.json` to open issues quickly.
- **Templates**: Use `templates/` and `scripts/generate_readme.py` for consistent project documentation.
- **Shared utilities**: Import from `shared/` package for common CLI patterns.

## Community & Learning

- Docs: see `docs/overview.md` and `docs/LEARNING_PATH.md`
- DSA Track: see `dsa/` for problems and tests
- Speed Rush: see `speed_rush/` for a 7-day plan
- Contribution Guide: `CONTRIBUTING.md` and `docs/CONTRIBUTING_GUIDE.md`
- Governance: `CODE_OF_CONDUCT.md` and `ROADMAP.md`

### Contributing Workflow

- Issues are labeled for quick onboarding: `good first issue`, `help wanted`, `docs`, `tests`.
- Open small, focused PRs. Use the PR template.
- Unsure where to start? Pick any `good first issue` or improve a README example.

## Hall of Fame (First-time Contributors)

See `CONTRIBUTORS.md`. Add your name in your first PR!

## Suggested Learning Path

- Start with Level 1 in order. Focus on reading input, loops, conditionals, and simple data structures.
- Move to Level 2. Practice file I/O, CSV/JSON, simple parsing, and small algorithms (minimax).
- Stretch tasks:
  - Add tests (pytest) for pure functions (e.g., calculator `calculate`, tictactoe `winner`).
  - Add docstrings and type hints across modules.
  - Refactor to packages with entry points.

## Contributing

See CONTRIBUTING.md for setup, style, and how to propose new beginner-friendly exercises.

## License

MIT – see LICENSE.
