# Expense Tracker (CSV)

Track and analyze expenses stored in a CSV file.

## How It Works

- Stores rows with `date, category, description, amount`
- `add`: append a new row after validating date and amount
- `list`: print all rows with running total
- `report`: group a month’s rows by category and sum amounts

## Example

```text
Date        Category       Amount   Description
------------------------------------------------------------
2025-01-03  groceries        24.90  Bread and milk
2025-01-05  transport        10.00  Bus pass
------------------------------------------------------------
Total: 34.90
```

## Internals

- CSV read/write helpers in `shared/path_utils.py`
- `Expense` dataclass for typed rows
- Simple aggregation with a dictionary keyed by category
