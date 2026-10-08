# portfolio.py
# Exercise 5: Stock Portfolio Tracker
# Skills: dicts, loops, nested loops
#
# portfolio is a "dict of dicts": each ticker maps to another dict
# holding that stock's shares and price. Access like portfolio["AAPL"]["price"].

import random

portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130},
}


def portfolio_value(port):
    """Total value = sum of (shares x price) for every stock."""
    total = 0
    for ticker, info in port.items():
        total += info["shares"] * info["price"]
    return total


# --- Part 1: current value ---
print("=== Current Portfolio ===")
for ticker, info in portfolio.items():
    value = info["shares"] * info["price"]
    print(f"{ticker}: {info['shares']} shares x ${info['price']:.2f} = ${value:,.2f}")
start_value = portfolio_value(portfolio)
print(f"Total value: ${start_value:,.2f}\n")

# --- Bonus: simulate a week (5 trading days) of random price moves ---
# random.seed(42)  # uncomment to get the same "random" results every run
print("=== One-Week Simulation (each price moves -5% to +5% per day) ===")
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
for day in days:                              # outer loop: each day
    for ticker, info in portfolio.items():    # inner loop: each stock
        change = random.uniform(-0.05, 0.05)  # e.g. 0.031 means +3.1%
        info["price"] = info["price"] * (1 + change)  # change builds on yesterday
    print(f"{day}: ${portfolio_value(portfolio):,.2f}")

end_value = portfolio_value(portfolio)
change_pct = (end_value - start_value) / start_value * 100
print(f"\nWeek change: ${end_value - start_value:+,.2f} ({change_pct:+.2f}%)")