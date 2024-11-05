from expense_management import add_expense, view_expenses, calculate_total_expenses
from monthly_reports import calculate_expenses_by_category
from file_handling import save_expenses_to_file, load_expenses_from_file

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses for a Month")
        print("4. Expenses by Category")
        print("5. Save Expenses to File")
        print("6. Load Expenses from File")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            month = input("Enter month: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_expense(month, category, description, amount)
            print("Expense added.")

        elif choice == "2":
            month = input("Enter month to view expenses: ")
            expenses = view_expenses(month)
            print(f"Expenses for {month}: {expenses}")

        elif choice == "3":
            month = input("Enter month to calculate total expenses: ")
            total = calculate_total_expenses(month)
            print(f"Total expenses for {month}: {total}")

        elif choice == "4":
            month = input("Enter month to calculate expenses by category: ")
            category_totals = calculate_expenses_by_category(month)
            print(f"Expenses by category for {month}: {category_totals}")

        elif choice == "5":
            filename = input("Enter filename to save expenses: ")
            save_expenses_to_file(filename)
            print("Expenses saved to file.")

        elif choice == "6":
            filename = input("Enter filename to load expenses: ")
            load_expenses_from_file(filename)
            print("Expenses loaded from file.")

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
