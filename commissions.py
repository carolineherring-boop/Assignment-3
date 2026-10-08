# commissions.py
# Exercise 4: Sales Commission Calculator
# Skills: for loop, functions
#
# Note: the assignment says "a list of sales" but the example is a DICTIONARY
# (name -> sales amount). We use the dictionary exactly as given.

sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}


def calculate_commission(sales_amount, rate=0.10):
    """Return the commission earned. Default rate is 10%."""
    return sales_amount * rate


# Build a new dict of name -> commission
commissions = {}
for name, amount in sales.items():
    commissions[name] = calculate_commission(amount)

# Rank from highest to lowest commission.
# key=lambda item: item[1] means "sort by the commission (2nd part of each pair)".
ranked = sorted(commissions.items(), key=lambda item: item[1], reverse=True)

print("=== Commission Leaderboard ===")
print(f"{'Rank':<6}{'Employee':<10}{'Sales':>10}{'Commission':>12}")
print("-" * 38)
rank = 1
for name, commission in ranked:
    print(f"{rank:<6}{name:<10}{'$' + format(sales[name], ','):>10}"
          f"{'$' + format(commission, ',.2f'):>12}")
    rank += 1