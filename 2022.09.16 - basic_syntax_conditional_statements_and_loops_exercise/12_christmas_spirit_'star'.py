quantity_of_decorations = int(input())
days_left_to_christmas = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

budget = 0
total_spirit = 0

for day in range(1, days_left_to_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        budget += ornament_set * quantity_of_decorations
        total_spirit += 5
    if day % 3 == 0:
        budget += (tree_garland + tree_skirt) * quantity_of_decorations
        total_spirit += 3 + 10
    if day % 5 == 0:
        budget += tree_lights * quantity_of_decorations
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        budget += (tree_skirt + tree_garland + tree_lights)
if days_left_to_christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
