number = int(input())
for i in range(number):
    num = int(input())
    if num == 88:
        print("Hello")
    elif num == 86:
        print("How are you?")
    elif num != 86 and num < 88:
        print("GREAT!")
    else:
        print("Bye.")