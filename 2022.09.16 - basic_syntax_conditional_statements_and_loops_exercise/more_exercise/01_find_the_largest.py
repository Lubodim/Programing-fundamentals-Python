number = input()
number_list = []
final_number = ""

for index in number:
    number_list.append(index)

while number_list:
    final_number += max(number_list)
    number_list.remove(max(number_list))

print(final_number)

