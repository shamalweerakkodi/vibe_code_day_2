def main():
    try:
        # Ask the user for total monthly budget
        total_budget_input = input("Enter your total monthly budget: ")
        total_budget = float(total_budget_input)

        total_expenses = 0.0
        
        # Enter expenses multiple times
        while True:
            expense_input = input("Enter an expense (or type 'done' to finish): ").strip().lower()
            
            # Stop entering when they type “done”
            if expense_input == "done":
                break
            
            try:
                expense = float(expense_input)
                total_expenses += expense
            except ValueError:
                print("Invalid input. Please enter a numeric value or 'done'.")

        # Subtract expenses from total budget
        remaining_balance = total_budget - total_expenses

        # Displays remaining balance
        print(f"\nTotal Budget: ${total_budget:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Balance: ${remaining_balance:.2f}")

        # Warning Message
        if remaining_balance < 500:
            print("Warning: Low Funds")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the total budget.")

if __name__ == "__main__":
    main()
