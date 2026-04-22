def calculate_bill(amount, tax):
    if amount < 0 or tax < 0:
        return "Invalid input"
    return amount + (amount * tax)
