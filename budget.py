import json
from datetime import datetime
from pathlib import Path


DATA_FILE = Path("data/transactions.json")


class BudgetTracker:
    def __init__(self):
        self.data = []
        self.load()

    def load(self):
        if not DATA_FILE.exists():
            self.data = []
            return

        try:
            with open(DATA_FILE, "r") as f:
                d = json.load(f)
                self.data = d if isinstance(d, list) else []
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved data.")
            self.data = []

    def save(self):
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(DATA_FILE, "w") as f:
                json.dump(self.data, f, indent=4)
        except OSError as e:
            print(f"Error saving data: {e}")

    @staticmethod
    def get_input(prompt):
        while True:
            value = input(prompt).strip()

            if value:
                return value

            print("This field cannot be blank.")

    @staticmethod
    def get_amount():
        while True:
            value = input("Amount: ").strip()

            try:
                amount = float(value)

                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                return amount

            except ValueError:
                print("Please enter a valid number.")

    @staticmethod
    def get_type():
        while True:
            value = input("Type (income/expense): ").strip().lower()

            match value:
                case "income":
                    return "income"
                case "expense":
                    return "expense"
                case _:
                    print("Please enter income or expense.")

    @staticmethod
    def get_date():
        while True:
            value = input(
                f"Date (YYYY-MM-DD) [{datetime.today().date()}]: "
            ).strip()

            if not value:
                return str(datetime.today().date())

            try:
                return datetime.strptime(
                    value, "%Y-%m-%d"
                ).date().isoformat()

            except ValueError:
                print("Invalid date. Use YYYY-MM-DD.")

    def add(self):
        t = {
            "id": self.next_id(),
            "type": self.get_type(),
            "amount": self.get_amount(),
            "category": self.get_input("Category: "),
            "date": self.get_date(),
            "note": input("Note (optional): ").strip()
        }

        self.data.append(t)
        self.save()
        print("Transaction added and saved.")

    def summary(self):
        income = sum(
            x["amount"]
            for x in self.data
            if x["type"] == "income"
        )

        expense = sum(
            x["amount"]
            for x in self.data
            if x["type"] == "expense"
        )

        return income, expense, income - expense

    def show_summary(self):
        income, expense, balance = self.summary()

        print("\n--- Summary ---")
        print(f"Total Income:   ₹{income:.2f}")
        print(f"Total Expenses: ₹{expense:.2f}")
        print(f"Net Balance:    ₹{balance:.2f}")

    def category(self):
        if not self.data:
            print("\nNo transactions found.")
            return

        cats = {}

        for x in self.data:
            cat = x["category"]

            if cat not in cats:
                cats[cat] = {
                    "income": 0.0,
                    "expense": 0.0
                }

            cats[cat][x["type"]] += x["amount"]

        print("\n--- By Category ---")

        for cat, total in sorted(cats.items()):
            print(
                f"{cat}: "
                f"Income ₹{total['income']:.2f}, "
                f"Expense ₹{total['expense']:.2f}"
            )

    def show(self):
        if not self.data:
            print("\nNo transactions found.")
            return False

        print("\n--- Transactions ---")

        for x in self.data:
            print(
                f"ID: {x['id']} | "
                f"{x['date']} | "
                f"{x['type']} | "
                f"₹{x['amount']:.2f} | "
                f"{x['category']} | "
                f"{x['note']}"
            )

        return True

    def delete(self):
        if not self.show():
            return

        while True:
            try:
                tid = int(input("Enter transaction ID to delete: "))
                break
            except ValueError:
                print("Please enter a valid ID.")

        for x in self.data:
            if x["id"] == tid:
                self.data.remove(x)
                self.save()
                print("Transaction deleted and saved.")
                return

        print("Transaction ID not found.")

    def edit(self):
        if not self.show():
            return

        while True:
            try:
                tid = int(input("Enter transaction ID to edit: "))
                break
            except ValueError:
                print("Please enter a valid ID.")

        for x in self.data:
            if x["id"] == tid:
                print("\nEnter the new transaction details.")

                x["type"] = self.get_type()
                x["amount"] = self.get_amount()
                x["category"] = self.get_input("Category: ")
                x["date"] = self.get_date()
                x["note"] = input("Note (optional): ").strip()

                self.save()
                print("Transaction edited and saved.")
                return

        print("Transaction ID not found.")

    def next_id(self):
        if not self.data:
            return 1

        return max(x["id"] for x in self.data) + 1

    def run(self):
        print("Welcome to Budget Tracker!")

        while True:
            print("\n1. Add transaction")
            print("2. View summary")
            print("3. View by category")
            print("4. Delete transaction")
            print("5. Edit transaction")
            print("6. Exit")

            choice = input("> ").strip()

            match choice:
                case "1":
                    self.add()
                case "2":
                    self.show_summary()
                case "3":
                    self.category()
                case "4":
                    self.delete()
                case "5":
                    self.edit()
                case "6":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice. Select 1-6.")


if __name__ == "__main__":
    app = BudgetTracker()
    app.run()
