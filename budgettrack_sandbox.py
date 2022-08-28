"""
Where I create and play with functions before adding it to the main budget_tracker.py file
"""

expense1 = {
    'water' : 250,
    'electric' : 150,
    'internet' : 150,
    'house insurance' : 400
}
expense2 = {
    'maintenance' : 300,
    'dog' : 250
}
expense_total = sum(expense1.values()) + sum(expense2.values())

income1 = {
    'salary' : 2500,
    'invest' : 1000
}
income2 = {
    'business' : 1000
}
income_total = sum(income1.values()) + sum(income2.values())

budget_plan = {
    'expenses' : 50,
    'savings' : 20,
    'wants' : 30
}

# write sandbox functions here
