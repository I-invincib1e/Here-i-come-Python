# Quiz Game

Multiple-choice quiz with JSON-based questions and a persistent top-10 highscore table.

## How It Works

- Loads `questions.json` (creates a default set if missing)
- Asks each question: displays choices and validates the answer
- Tracks score and then prompts for a name
- Saves score to `highscores.json`, keeping the top 10

## Example

```text
Q1. What is the capital of France?
  1) Berlin
  2) Madrid
  3) Paris
  4) Lisbon
Your answer (1-4): 3
Correct!
```

## Internals

- Uses helpers in `shared/path_utils.py` for JSON I/O
- `Question` dataclass defines each quiz item
- Highscores sorted by score desc, then name
