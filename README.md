# Budget_tracker
Budget Tracker CLI
A Python 3 command-line budget tracker for recording income and expenses.

Project structure
budget_tracker/
├── budget.py
├── README.md
└── data/
    └── transactions.json
Requirements
Python 3.x
No external packages are required.
The program uses Python's built-in json, datetime, and pathlib modules.
How to run
Open a terminal in the budget_tracker folder and run:

python budget.py
On some systems:

python3 budget.py
Menu
Add transaction — records income/expense, amount, category, date and optional note.
View summary — displays total income, total expenses and net balance.
View by category — shows income and expenses grouped by category.
Delete transaction — removes a transaction using its ID.
Edit transaction — updates an existing transaction.
Exit — closes the program.
Data storage
Transactions are stored in data/transactions.json.
