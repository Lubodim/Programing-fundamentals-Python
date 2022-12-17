tank_capacity = 255
number_of_lines = int(input())
liters_of_watter = tank_capacity
liters = 0
for lines in range(number_of_lines):
    current_litres = int(input())
    if current_litres <= liters_of_watter:
        liters_of_watter -= current_litres
        liters += current_litres
    else:
        print("Insufficient capacity!")
print(liters)
