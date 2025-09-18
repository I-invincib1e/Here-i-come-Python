# Simple Calculator (CLI)

A tiny REPL that parses and evaluates expressions using `+ - * / ^`.

## How It Works

- Input format: `<number> <operator> <number>` (tokens separated by spaces)
- Parsing: splits the input into three tokens and validates types
- Dispatch: picks the operator function from a dictionary
- Safety: rejects division by zero and unknown operators

## Example

```text
> 2 + 3
5
> 2 ^ 10
1024
```

## Internals

- Core functions: `get_operations()`, `calculate(expr)`
- Operators are mapped to Python’s `operator` functions
- Errors are shown as simple messages in the REPL

## Notes

- Operators require spaces (e.g., `2 + 3`, not `2+3`)
