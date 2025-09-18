from __future__ import annotations

import operator
from typing import Callable, Dict

from shared.cli_utils import create_repl_loop


def get_operations() -> Dict[str, Callable[[float, float], float]]:
    return {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "^": operator.pow,
    }


def calculate(expr: str) -> float:
    tokens = expr.strip().split()
    if len(tokens) != 3:
        raise ValueError("Use format: <number> <op> <number> e.g., 2 + 3")

    left_str, op, right_str = tokens
    try:
        left = float(left_str)
        right = float(right_str)
    except ValueError as exc:
        raise ValueError("Operands must be numbers") from exc

    operations = get_operations()
    if op not in operations:
        raise ValueError(f"Unsupported operator '{op}'. Supported: {', '.join(operations)}")

    if op == "/" and right == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return operations[op](left, right)


def process_calculation(expr: str) -> None:
    """Process a single calculation expression."""
    try:
        result = calculate(expr)
        print(result)
    except Exception as exc:  # noqa: BLE001 - simple CLI surfacing errors
        print(f"Error: {exc}")


def repl() -> None:
    welcome = "Simple Calculator CLI\nEnter expressions like: 2 + 3  |  4 * 5  |  2 ^ 10"
    create_repl_loop(process_calculation, welcome, "> ")


if __name__ == "__main__":
    repl()


