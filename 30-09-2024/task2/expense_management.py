expenses = {}

def add_expense(month, category, description, amount):
    """Adds an expense to the specified month."""
    expense = (category, description, amount)
    if month not in expenses:
        expenses[month] = []
    expenses[month].append(expense)

def view_expenses(month):
    """Returns the list of expenses for the specified month."""
    return expenses.get(month, [])

def calculate_total_expenses(month):
    """Calculates the total expenses for the specified month."""
    total = sum(expense[2] for expense in view_expenses(month))
    return total
