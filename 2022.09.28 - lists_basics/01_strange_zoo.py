strange_zoo_list = []

for _ in range(3):
    part_of_zoo = input()
    strange_zoo_list.append(part_of_zoo)

strange_zoo_list[0], strange_zoo_list[2] = strange_zoo_list[2], strange_zoo_list[0]

print(strange_zoo_list)
