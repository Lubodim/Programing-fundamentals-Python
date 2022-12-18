number = int(input())

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

int_list = []

for _ in range(number):
    current_number = int(input())
    int_list.append(current_number)

command = input()

filterd_list = []

for num in int_list:
    filterd_passes = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )
    if filterd_passes:
        filterd_list.append(num)

print(filterd_list)
