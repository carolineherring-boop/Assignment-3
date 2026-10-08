# pitch_chart.py
# Exercise 10: Startup Pitch Deck Visualizer (ASCII Style)
# Skills: nested loops, string multiplication
#
# Real revenue numbers are too big to print as that many # symbols, so we
# SCALE them: each "#" stands for a fixed amount of money.

revenues = [30000, 50000, 80000, 120000, 175000]  # projected revenue, years 1-5
dollars_per_hash = 10000  # each # = $10,000

# --- Version 1: horizontal bars with string multiplication ---
print("Projected revenue by year (each # = $10,000):\n")
year = 1
for amount in revenues:
    bar_length = round(amount / dollars_per_hash)
    print(f"Year {year}: {'#' * bar_length}  ${amount:,}")  # "#" * 3 -> "###"
    year += 1

# --- Version 2: vertical bars with NESTED loops ---
# Outer loop = rows from the top of the chart down.
# Inner loop = one column per year: print "#" if that bar reaches this row.
print("\nSame data as a vertical chart:\n")
heights = []
for amount in revenues:
    heights.append(round(amount / dollars_per_hash))

tallest = max(heights)
for row in range(tallest, 0, -1):        # e.g. 18, 17, ..., 1
    line = ""
    for h in heights:
        line += "  #  " if h >= row else "     "
    print(line)

# Labels under the columns
labels = ""
for i in range(1, len(heights) + 1):
    labels += f" Y{i}  "
print("-" * len(labels))
print(labels)