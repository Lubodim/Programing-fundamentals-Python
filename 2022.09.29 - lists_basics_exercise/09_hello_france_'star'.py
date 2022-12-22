product_list = input().split("|")
budged = int(input())
working_money = budged
needed_money = 150
new_product_list = []
new_money = []
for element in product_list:
    element = element.split("->")
    item = element[0]
    price = float(element[1])
    if item == "Clothes" and price > 50 \
            or item == "Shoes" and price > 35 \
            or item == "Accessories" and price > 20.5:
        continue
    if working_money >= price:
        working_money -= price
        new_product_list.append(price)
        price *= 1.4   # increase 40% for sale
        print(f"{price:.2f}", end=" ")
        new_money.append(price)
print()
profit = sum(new_money) - sum(new_product_list)
print(f"Profit: {profit:.2f}")
if sum(new_money) + working_money > needed_money:
    print("Hello, France!")
else:
    print("Not enough money.")
