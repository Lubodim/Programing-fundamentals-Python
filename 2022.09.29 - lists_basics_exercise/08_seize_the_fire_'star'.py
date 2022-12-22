fire_list = input().split("#")
water = int(input())
cill_is_valide = False
spend_water = []
for fire in fire_list:
    cell_range = fire.split(" ")
    type_cell = cell_range[0]
    volume = int(cell_range[2])
    if type_cell == "High" and 81 <= volume <= 125:
        cill_is_valide = True
    elif type_cell == "Medium" and 51 <= volume <= 80:
        cill_is_valide = True
    elif type_cell == "Low" and 1 <= volume <= 50:
        cill_is_valide = True
    else:
        continue
    if cill_is_valide:
        if volume <= water:
            spend_water.append(volume)
            water -= volume
efforit = sum(spend_water) * 0.25

print("Cells:")
for vol in spend_water:
    print(f" - {vol}")
print(f"Effort: {efforit:.2f}")
print(f"Total Fire: {sum(spend_water)}")
