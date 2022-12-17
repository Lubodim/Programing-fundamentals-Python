number_of_people = int(input())
capacity_of_elevator = int(input())

result = number_of_people // capacity_of_elevator
if number_of_people % capacity_of_elevator != 0:
    result += 1
print(result)
