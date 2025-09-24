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

## Industry Applications

**Where Calculator Logic is Used in the Real World:**

- **Financial Software**: Banks and fintech apps use similar expression evaluation for interest calculations, loan payments, and investment formulas
- **Scientific Computing**: Research software evaluates mathematical expressions for simulations, data analysis, and computational models
- **E-commerce Platforms**: Price calculations, tax computations, and discount applications use arithmetic expression parsing
- **Spreadsheet Applications**: Excel, Google Sheets use similar logic for formula evaluation and cell calculations
- **Engineering Tools**: CAD software, simulation tools evaluate mathematical expressions for design calculations
- **Data Science**: Pandas, NumPy libraries perform vectorized arithmetic operations similar to this calculator's logic

**Learning Connection:** This simple calculator demonstrates the foundation of expression evaluation used in complex systems like database query engines, programming language interpreters, and financial trading platforms.

## Notes

- Operators require spaces (e.g., `2 + 3`, not `2+3`)
