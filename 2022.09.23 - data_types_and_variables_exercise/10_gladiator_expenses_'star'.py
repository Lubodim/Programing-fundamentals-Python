lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
broken_shield_counter = 0
for lost_fight_day in range(1, lost_fights + 1):
    if lost_fight_day % 2 == 0:
        expenses += helmet_price
    if lost_fight_day % 3 == 0:
        expenses += sword_price
    if lost_fight_day % 2 == 0 and lost_fight_day % 3 == 0:
        expenses += shield_price
        broken_shield_counter += 1
        if broken_shield_counter % 2 == 0:
            expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
