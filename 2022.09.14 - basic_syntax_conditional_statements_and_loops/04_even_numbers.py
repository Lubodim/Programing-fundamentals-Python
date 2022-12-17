number = int(input())
is_odd = False

for i in range(number):
    num = int(input())
    if num % 2 != 0:
        is_odd = True
        print(f"{num} is odd!")
        break
if not is_odd:
    print("All numbers are even.")
