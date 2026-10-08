# loyalty_tiers.py
# Exercise 8: Customer Loyalty Tiers
# Skills: conditionals, dicts, loops
#
# Tier rules:
#   Bronze: under $1,000
#   Silver: $1,000 up to (but not including) $5,000
#   Gold:   $5,000 and above

customers = {
    "Ana": 450.00,
    "Ben": 1000.00,   # exactly 1000 -> Silver
    "Cleo": 4999.99,  # just under 5000 -> Silver
    "Dev": 5000.00,   # exactly 5000 -> Gold
    "Eli": 12500.00,
    "Fay": 820.50,
}


def get_tier(amount):
    """Return the loyalty tier for a total purchase amount."""
    if amount >= 5000:
        return "Gold"
    elif amount >= 1000:
        return "Silver"
    else:
        return "Bronze"


tier_counts = {"Bronze": 0, "Silver": 0, "Gold": 0}

print("=== Customer Tiers ===")
for name, total in customers.items():
    tier = get_tier(total)
    tier_counts[tier] += 1
    print(f"{name:<6}${total:>10,.2f}  {tier}")

print("\n=== Tier Summary ===")
for tier, count in tier_counts.items():
    label = "customer" if count == 1 else "customers"
    print(f"{tier:<7}{count} {label}")