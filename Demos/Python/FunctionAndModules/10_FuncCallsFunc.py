def calculate_total(price, quantity):
    return price * quantity

def calculate_tax(amount):
    return amount * 0.18

def calculate_bill(price, quantity):
    total = calculate_total(price, quantity)
    tax = calculate_tax(total)
    return total + tax

bill = calculate_bill(1000, 2)
print(f"Final Bill Amount: {bill}")