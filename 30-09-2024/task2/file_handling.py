import json
from expense_management import expenses

def save_expenses_to_file(filename):
    """Saves expenses to a file in JSON format."""
    with open(filename, 'w') as file:
        json.dump(expenses, file)

def load_expenses_from_file(filename):
    """Loads expenses from a file."""
    global expenses
    with open(filename, 'r') as file:
        expenses = json.load(file)
