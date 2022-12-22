easter_gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        break
    command = list(command.split())
    if command[0] == "OutOfStock":
        for word in range(len(easter_gifts)):
            if command[1] in easter_gifts:
                if easter_gifts[word] == command[1]:
                    easter_gifts[word] = "None"
    elif command[0] == "Required":
        if 0 < int(command[2]) < len(easter_gifts):
            replace_index = int(command[2])
            easter_gifts[replace_index] = command[1]
    elif command[0] == "JustInCase":
        easter_gifts[-1] = command[1]

for printing in easter_gifts:
    if printing != "None":
        print(printing, end=" ")
