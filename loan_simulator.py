# loan_simulator.py
# Exercise 6: Bank Loan Repayment Simulator
# Skills: while loops, math, functions
#
# Assumption: the interest rate entered is an ANNUAL percentage (e.g. 6 for 6%),
# which is how banks quote it. Interest is charged monthly at rate / 12.


def get_number(prompt):
    """Keep asking until the user enters a valid non-negative number."""
    while True:
        text = input(prompt).strip().replace("$", "").replace("%", "").replace(",", "")
        if text.replace(".", "", 1).isdigit():
            return float(text)
        print("  Please enter a valid number.")


def simulate_loan(balance, annual_rate, payment):
    """Simulate month-by-month repayment. Returns (months, total_interest).
    Returns (None, None) if the payment can never pay off the loan."""
    monthly_rate = annual_rate / 100 / 12

    # Guard against an infinite loop: if the payment doesn't even cover the
    # first month's interest, the balance grows forever.
    if payment <= balance * monthly_rate:
        return None, None

    months = 0
    total_interest = 0
    while balance > 0:
        interest = balance * monthly_rate
        balance = balance + interest
        total_interest += interest
        balance = balance - min(payment, balance)  # last payment may be smaller
        months += 1
        if months <= 3 or balance == 0:
            print(f"  Month {months:>3}: interest ${interest:,.2f}, balance ${balance:,.2f}")
        elif months == 4:
            print("  ...")
    return months, total_interest


print("=== Loan Repayment Simulator ===")
loan = get_number("Loan amount: $")
rate = get_number("Annual interest rate (%): ")
payment = get_number("Monthly payment: $")
print()

months, interest_paid = simulate_loan(loan, rate, payment)

if months is None:
    print("That payment is too small: it doesn't cover the monthly interest,")
    print("so the loan would never be paid off. Try a larger payment.")
else:
    years = months // 12
    extra = months % 12
    print(f"\nPaid off in {months} months ({years} years, {extra} months).")
    print(f"Total interest paid: ${interest_paid:,.2f}")