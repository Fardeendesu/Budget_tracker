# Budget Tracker CLI

A Python 3 command-line budget tracker for recording income and expenses.

## Project structure

```text
budget_tracker/
├── budget.py
├── README.md
└── data/
    └── transactions.json
```

## Requirements

- Python 3.x
- No external packages are required.
- The program uses Python's built-in `json`, `datetime`, and `pathlib` modules.

## How to run

Open a terminal in the `budget_tracker` folder and run:

```bash
python budget.py
```

On some systems:

```bash
python3 budget.py
```

## Menu

1. **Add transaction** — records income/expense, amount, category, date and optional note.
2. **View summary** — displays total income, total expenses and net balance.
3. **View by category** — shows income and expenses grouped by category.
4. **Delete transaction** — removes a transaction using its ID.
5. **Edit transaction** — updates an existing transaction.
6. **Exit** — closes the program.

## Data storage

Transactions are stored in `data/transactions.json`.
