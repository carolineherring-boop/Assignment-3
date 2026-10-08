# survey.py
# Exercise 2: Market Survey Analyzer
# Skills: for loop, dicts, counting
#
# "Fake survey data" just means YOU make up a list of answers to analyze.

responses = ["coffee", "tea", "coffee", "soda",
             "Coffee", " tea ", "juice", "coffee"]

# Step 1: count each product with a dictionary  {product: count}
counts = {}
for answer in responses:
    product = answer.strip().lower()  # " Coffee " and "coffee" count as the same
    if product in counts:
        counts[product] += 1
    else:
        counts[product] = 1
    # Shortcut version of the 4 lines above: counts[product] = counts.get(product, 0) + 1

total = len(responses)

# Step 2: print a market-share summary, most popular first
print("=== Market Share Summary ===")
print(f"Total responses: {total}\n")

# sorted(..., key=..., reverse=True) orders the (product, count) pairs by count,
# highest first. item[1] is the count part of each pair.
for product, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    share = count / total * 100
    print(f"{product}: {share:.1f}%  ({count} of {total})")