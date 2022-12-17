number = int(input())
for i in range(number):
    string = input()
    is_not_pure = False
    for j in string:
        if j == "," or j == "." or j == "_":
            is_not_pure = True
    if not is_not_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
