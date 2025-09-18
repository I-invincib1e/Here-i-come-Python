# Python Learning Guide: Practice Projects

![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Beginner Friendly](https://img.shields.io/badge/beginner-friendly-blue)
![Educational](https://img.shields.io/badge/educational-learning-orange)

**Master Python programming through hands-on practice.** Build small, focused programs that teach fundamental concepts, best practices, and problem-solving skills. All projects use only the Python standard library for maximum learning value.

## 🎯 Learning Objectives

- **Core Python Skills**: Variables, functions, loops, conditionals, file I/O
- **Problem Solving**: Break down problems into manageable steps
- **Code Organization**: Structure programs with clear, readable code
- **Testing & Debugging**: Write robust code that handles edge cases
- **Best Practices**: Follow Python conventions and documentation standards

## Requirements

- Python 3.8+
- Windows PowerShell or a Unix shell (macOS/Linux)

## Run a Project

From the repository root:

- Windows: `python .\\basic_programs\\<project>\\main.py`
- macOS/Linux: `python3 ./basic_programs/<project>/main.py`

Or use the launcher:

- Windows: `python .\\launcher.py`
- macOS/Linux: `python3 ./launcher.py`

## Projects (`basic_programs/`)

- guess_number – Guess a number between 1–100
- calculator_cli – Simple REPL calculator (+ - * / ^)
- todo_cli – Minimal todo list (add/list/done/del)
- stopwatch_cli – Stopwatch with laps
- rock_paper_scissors – Play vs computer
- tictactoe_ai – Tic Tac Toe vs simple AI
- expense_tracker – CSV expense tracker
- file_organizer – Sort files by type (supports --dry-run)
- md_notes – Markdown notes manager
- quiz_game – Multiple-choice quiz

## Learn More

- Overview: `index.md`
- DSA guide: `dsa/LEARNING_GUIDE.md`
- Good first tasks: `GOOD_FIRST_ISSUES.md`
- How to contribute: `CONTRIBUTING.md`

## Notebooks (optional)

If you like notebooks:

1. Install dev tools:

```bash
pip install -e .[dev]
```

1. Start Jupyter:

```bash
jupyter notebook
```

Then open files in `notebooks/`.

## License

MIT – see `LICENSE`.
