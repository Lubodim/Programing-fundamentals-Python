while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    for i in command:
        print(i * 2, end="")
    print()
