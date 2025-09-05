from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Iterable, List


DATA_FILE = Path(__file__).with_name("expenses.csv")


@dataclass
class Expense:
    when: date
    category: str
    description: str
    amount: float


def parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def load_expenses() -> List[Expense]:
    if not DATA_FILE.exists():
        return []
    rows: List[Expense] = []
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(
                Expense(
                    when=parse_date(r["date"]),
                    category=r["category"],
                    description=r["description"],
                    amount=float(r["amount"]),
                )
            )
    return rows


def save_expenses(rows: Iterable[Expense]) -> None:
    with DATA_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "category", "description", "amount"])
        writer.writeheader()
        for e in rows:
            writer.writerow(
                {
                    "date": e.when.strftime("%Y-%m-%d"),
                    "category": e.category,
                    "description": e.description,
                    "amount": f"{e.amount:.2f}",
                }
            )


def add_expense(when_str: str, category: str, amount_str: str, description: str) -> None:
    rows = load_expenses()
    rows.append(Expense(parse_date(when_str), category, description, float(amount_str)))
    save_expenses(rows)
    print("Added.")


def list_expenses() -> None:
    rows = load_expenses()
    if not rows:
        print("No expenses yet.")
        return
    total = 0.0
    print("Date        Category       Amount   Description")
    print("-" * 60)
    for e in rows:
        total += e.amount
        print(f"{e.when}  {e.category:<13}  {e.amount:>7.2f}  {e.description}")
    print("-" * 60)
    print(f"Total: {total:.2f}")


def report_month(year: int, month: int) -> None:
    rows = load_expenses()
    filtered = [e for e in rows if e.when.year == year and e.when.month == month]
    if not filtered:
        print("No expenses for that month.")
        return
    by_cat = {}
    for e in filtered:
        by_cat[e.category] = by_cat.get(e.category, 0.0) + e.amount
    print(f"Report {year}-{month:02}")
    for cat, amt in sorted(by_cat.items(), key=lambda x: -x[1]):
        print(f"{cat:<15} {amt:>8.2f}")
    print(f"Total: {sum(by_cat.values()):.2f}")


def help_text() -> None:
    print("Expense Tracker")
    print("Commands:")
    print("  add <YYYY-MM-DD> <category> <amount> <description...>")
    print("  list")
    print("  report <YYYY> <MM>")


def main(argv: List[str]) -> None:
    if not argv or argv[0] in {"help", "-h", "--help"}:
        help_text()
        return
    cmd = argv[0]
    if cmd == "add":
        if len(argv) < 5:
            print("Usage: add <YYYY-MM-DD> <category> <amount> <description...>")
            return
        add_expense(argv[1], argv[2], argv[3], " ".join(argv[4:]))
    elif cmd == "list":
        list_expenses()
    elif cmd == "report":
        if len(argv) != 3 or not (argv[1].isdigit() and argv[2].isdigit()):
            print("Usage: report <YYYY> <MM>")
            return
        report_month(int(argv[1]), int(argv[2]))
    else:
        print("Unknown command. Type 'help' for usage.")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])


