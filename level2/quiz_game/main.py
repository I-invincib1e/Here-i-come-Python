from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import List


QUESTIONS_FILE = Path(__file__).with_name("questions.json")
HIGHSCORES_FILE = Path(__file__).with_name("highscores.json")


@dataclass
class Question:
    prompt: str
    choices: List[str]
    answer_index: int


def load_questions() -> List[Question]:
    if not QUESTIONS_FILE.exists():
        default = [
            {
                "prompt": "What is the capital of France?",
                "choices": ["Berlin", "Madrid", "Paris", "Lisbon"],
                "answer_index": 2,
            },
            {
                "prompt": "2 + 2 = ?",
                "choices": ["3", "4", "5", "22"],
                "answer_index": 1,
            },
        ]
        QUESTIONS_FILE.write_text(json.dumps(default, indent=2), encoding="utf-8")
    data = json.loads(QUESTIONS_FILE.read_text(encoding="utf-8"))
    return [Question(**q) for q in data]


def ask_questions(questions: List[Question]) -> int:
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Q{i}. {q.prompt}")
        for idx, choice in enumerate(q.choices):
            print(f"  {idx + 1}) {choice}")
        while True:
            ans = input("Your answer (1-4): ").strip()
            if ans.isdigit() and 1 <= int(ans) <= len(q.choices):
                break
            print("Invalid choice. Try again.")
        if int(ans) - 1 == q.answer_index:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Correct is {q.answer_index + 1}. {q.choices[q.answer_index]}\n")
    return score


def save_highscore(name: str, score: int, total: int) -> None:
    entry = {"name": name, "score": score, "total": total}
    if HIGHSCORES_FILE.exists():
        data = json.loads(HIGHSCORES_FILE.read_text(encoding="utf-8"))
    else:
        data = []
    data.append(entry)
    data.sort(key=lambda x: (-x["score"], x["name"]))
    data = data[:10]
    HIGHSCORES_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def show_highscores() -> None:
    if not HIGHSCORES_FILE.exists():
        print("No highscores yet.")
        return
    data = json.loads(HIGHSCORES_FILE.read_text(encoding="utf-8"))
    print("Top 10 Highscores:")
    for i, e in enumerate(data, 1):
        print(f"{i:2}. {e['name']:<10} {e['score']}/{e['total']}")


def main() -> None:
    print("Quiz Game")
    questions = load_questions()
    score = ask_questions(questions)
    print(f"Your score: {score}/{len(questions)}")
    name = input("Enter your name for the highscore table (or leave blank): ").strip() or "Anonymous"
    save_highscore(name, score, len(questions))
    print()
    show_highscores()


if __name__ == "__main__":
    main()


