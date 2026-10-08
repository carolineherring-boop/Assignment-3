# checkout.py
# Exercise 1: Retail Checkout Simulation
# Skills: while loop, input validation, lists
#
# The customer enters item prices one at a time. Entering 0 ends checkout.
# Then the program prints the total, average item cost, and number of items.


def get_price(prompt):
    """Keep asking until the user types a valid, non-negative number."""
    while True:
        text = input(prompt).strip().replace("$", "")  # allow "$4.99"
        # "4.99".replace(".", "", 1) -> "499", which isdigit() accepts.
        # This rejects letters, blanks, and negatives without using try/except.
        if text.replace(".", "", 1).isdigit():
            return float(text)
        print("  Invalid entry. Please type a price like 4.99 (or 0 to finish).")


prices = []  # every valid price gets stored here

print("=== Retail Checkout ===")
print("Enter item prices one at a time. Enter 0 when you are done.\n")

while True:
    price = get_price(f"Item {len(prices) + 1} price: $")
    if price == 0:  # sentinel value: 0 means "I'm finished"
        break
    prices.append(price)

print("\n=== Receipt ===")
if len(prices) == 0:
    # Guard: without this, the average would divide by zero.
    print("No items purchased.")
else:
    total = 0
    for p in prices:  # add up the list by hand (sum(prices) does the same)
        total += p

    count = len(prices)
    average = total / count

    print(f"Number of items: {count}")
    print(f"Total purchase:  ${total:,.2f}")
    print(f"Average item:    ${average:,.2f}")