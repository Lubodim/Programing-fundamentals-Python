are_sorted_successfully = True

while True:
    command = input()
    if command == "Welcome!":
        break
    if command == "Voldemort":
        are_sorted_successfully = False
        print("You must not speak of that name!")
        break
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")
if are_sorted_successfully:
    print("Welcome to Hogwarts.")
