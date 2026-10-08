# supply_chain.py
# Exercise 7: Simple Supply Chain Tracker
# Skills: nested loops, lists of dicts
#
# warehouses is a LIST; each item is a DICT; inside it, "inventory" is another DICT.
# Outer loop walks the warehouses; inner loop walks one warehouse's products.

warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}},
    {"name": "Warehouse C", "inventory": {"apples": 50, "oranges": 75}},  # added to show a new product
]

totals = {}  # product -> total quantity across ALL warehouses

for warehouse in warehouses:                                  # outer loop
    print(f"{warehouse['name']}:")
    for product, qty in warehouse["inventory"].items():       # inner loop
        print(f"  {product:<10}{qty:>6}")
        totals[product] = totals.get(product, 0) + qty         # start at 0 if new

print("\n=== Total Stock Across Supply Chain ===")
for product, qty in totals.items():
    print(f"{product:<10}{qty:>6}")