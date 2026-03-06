def main():
    try:
        # Ask the user for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))

        # Ask for 3 expenses
        expense1 = float(input("Enter expense 1: "))
        expense2 = float(input("Enter expense 2: "))
        expense3 = float(input("Enter expense 3: "))

        # Subtract expenses from total budget
        total_expenses = expense1 + expense2 + expense3
        remaining_balance = total_budget - total_expenses

        # Displays remaining balance
        print(f"\nTotal Budget: ${total_budget:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Balance: ${remaining_balance:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for budget and expenses.")

if __name__ == "__main__":
    main()
