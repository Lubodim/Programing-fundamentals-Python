number_orders = int(input())
total_price = 0

for _ in range(number_orders):
    is_out_of_range = False
    price = 0
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100.00:
        is_out_of_range = True
    if 1 > days or days > 31:
        is_out_of_range = True
    if 1 > needed_capsules_per_day or needed_capsules_per_day > 2000:
        is_out_of_range = True
    price += price_per_capsule * days * needed_capsules_per_day
    if not is_out_of_range:
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
