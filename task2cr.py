import json

# Initialize data structures
budget = {'income': 0, 'expenses': []}

# Load budget data from a file if available
try:
    with open('budget_data.json', 'r') as file:
        budget = json.load(file)
except FileNotFoundError:
    pass

def save_budget_data():
    with open('budget_data.json', 'w') as file:
        json.dump(budget, file)

def main():
    while True:
        # Display menu and get user choice
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add income
            amount = float(input("Enter income amount: "))
            budget['income'] += amount
        elif choice == '2':
            # Add expense
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget['expenses'].append({'category': category, 'amount': amount})
        elif choice == '3':
            # Calculate budget
            remaining_budget = budget['income'] - sum(expense['amount'] for expense in budget['expenses'])
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == '4':
            # Analyze expenses (you can expand this)
            expense_categories = set(expense['category'] for expense in budget['expenses'])
            for category in expense_categories:
                total_expense = sum(expense['amount'] for expense in budget['expenses'] if expense['category'] == category)
                print(f"{category}: ${total_expense}")
        elif choice == '5':
            # Save data and exit
            save_budget_data()
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
