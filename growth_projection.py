# growth_projection.py
# Exercise 9: Business Growth Projection
# Skills: for loops, math
#
# Each year's revenue = last year's revenue x (1 + growth rate).
# A "5%" growth rate must be converted to 0.05 before doing the math.


def get_number(prompt):
    """Keep asking until the user enters a valid non-negative number."""
    while True:
        text = input(prompt).strip().replace("$", "").replace("%", "").replace(",", "")
        if text.replace(".", "", 1).isdigit():
            return float(text)
        print("  Please enter a valid number.")


print("=== 10-Year Revenue Projection ===")
revenue = get_number("Initial (Year 0) revenue: $")
growth_pct = get_number("Annual growth rate (%): ")
growth = growth_pct / 100  # 5 -> 0.05

start = revenue
print(f"\n{'Year':<6}{'Revenue':>18}{'Growth ($)':>16}")
print("-" * 40)
print(f"{0:<6}{'$' + format(revenue, ',.2f'):>18}{'-':>16}")

for year in range(1, 11):  # range(1, 11) gives 1, 2, ..., 10
    previous = revenue
    revenue = revenue * (1 + growth)
    print(f"{year:<6}{'$' + format(revenue, ',.2f'):>18}"
          f"{'$' + format(revenue - previous, ',.2f'):>16}")

print("-" * 40)
print(f"Revenue grows {revenue / start:.2f}x over 10 years at {growth_pct:g}% per year.")