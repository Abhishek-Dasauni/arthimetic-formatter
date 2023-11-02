class Budget:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.expenses = []

    def add_income(self, amount):
        self.balance += amount

    def add_expense(self, category, amount):
        self.expenses.append((category, amount))
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_expenses(self):
        return self.expenses

    def generate_expense_report(self):
        report = "Expense Report:\n"
        for category, amount in self.expenses:
            report += f"- {category}: ${amount:.2f}\n"
        return report


def main():
    budget = Budget()

    while True:
        print("\nBudget App Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Check Balance")
        print("4. Generate Expense Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            income = float(input("Enter the income amount: $"))
            budget.add_income(income)
            print(f"Income of ${income:.2f} added successfully.")

        elif choice == "2":
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: $"))
            budget.add_expense(category, amount)
            print(f"Expense of ${amount:.2f} in '{category}' category added successfully.")

        elif choice == "3":
            balance = budget.get_balance()
            print(f"Current Balance: ${balance:.2f}")

        elif choice == "4":
            expense_report = budget.generate_expense_report()
            print(expense_report)

        elif choice == "5":
            print("Exiting the Budget App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
