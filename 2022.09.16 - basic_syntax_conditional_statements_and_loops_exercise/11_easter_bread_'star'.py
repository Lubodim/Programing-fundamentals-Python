budget = float(input())
price_per_kilo_flour = float(input())
eggs_pack = price_per_kilo_flour * 0.75
quarter_milk_price = (price_per_kilo_flour * 1.25) / 4
money_in_wallet = budget
ester_bread = price_per_kilo_flour + eggs_pack + quarter_milk_price
ester_bread_counter = 0
colored_eggs = 0

while money_in_wallet > ester_bread:
    if money_in_wallet == 0:
        break
    money_in_wallet -= ester_bread
    ester_bread_counter += 1
    colored_eggs += 3
    if ester_bread_counter % 3 == 0:
        colored_eggs -= ester_bread_counter - 2
print(f"You made {ester_bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_in_wallet:.2f}BGN left.")