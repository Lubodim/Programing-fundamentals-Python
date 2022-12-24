
def order(product: str, quant: int):
    result = None
    if product == "coffee":
        result = quant * 1.5  # price of coffee
    elif product == "coke":
        result = quant * 1.4  # price ot coke
    elif product == "water":
        result = quant * 1  # price ot water
    elif product == "snacks":
        result = quant * 2  # price ot snacks
    return (f"{result:.2f}")

order_product = input()
quantity = int(input())

print(order(order_product, quantity))
