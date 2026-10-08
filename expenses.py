# expenses.py
# Exercise 3: Expense Report Categorizer
# Skills: nested loops, dicts
#
# Each category (key) holds a LIST of individual expenses (value).
# Outer loop = categories, inner loop = the expenses inside one category.

expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100],
}

grand_total = 0
category_totals = {}

for category, amounts in expenses.items():  # outer loop: each category
    category_total = 0
    for amount in amounts:                   # inner loop: each expense in it
        category_total += amount
    category_totals[category] = category_total
    grand_total += category_total

# Print a neat report
print("=" * 36)
print("       EXPENSE SUMMARY REPORT")
print("=" * 36)
print(f"{'Category':<12}{'Items':>8}{'Total':>16}")
print("-" * 36)
for category, total in category_totals.items():
    num_items = len(expenses[category])
    print(f"{category:<12}{num_items:>8}{'$' + format(total, ',.2f'):>16}")
print("-" * 36)
print(f"{'GRAND TOTAL':<20}{'$' + format(grand_total, ',.2f'):>16}")
print("=" * 36)