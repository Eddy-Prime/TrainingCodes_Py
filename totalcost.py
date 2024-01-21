def total_cost(amount):
    if amount < 100:
        return amount + 10
    elif amount >= 200:
        return amount - (0.05 * amount)
    else:
        return amount

amount = float(input("Enter amount: "))
print(total_cost(amount))