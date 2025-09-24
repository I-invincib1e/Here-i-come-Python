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

## Industry Applications

**Where Expense Tracking Logic is Used in the Real World:**

- **Financial Software**: Mint, YNAB, QuickBooks use similar data structures for transaction processing and categorization
- **E-commerce Analytics**: Amazon, Shopify track order values, shipping costs, and revenue by category
- **Business Intelligence**: Tableau, Power BI aggregate sales data by time periods and product categories
- **Banking Systems**: Core banking applications process millions of transactions daily with similar grouping logic
- **Accounting Software**: SAP, Oracle Financials use CSV/Excel imports for expense reporting and tax calculations
- **Data Warehousing**: ETL processes in companies like Airbnb, Uber aggregate operational metrics by categories

**Learning Connection:** This expense tracker demonstrates the foundation of data aggregation used in enterprise systems. The same patterns power financial dashboards, sales analytics, and operational reporting in Fortune 500 companies.

## Internals

- CSV read/write helpers in `shared/path_utils.py`
- `Expense` dataclass for typed rows
- Simple aggregation with a dictionary keyed by category
