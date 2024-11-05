from expense_management import view_expenses

def calculate_expenses_by_category(month):
    """Calculates expenses by category for the specified month."""
    category_totals = {}
    for category, description, amount in view_expenses(month):
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return category_totals
