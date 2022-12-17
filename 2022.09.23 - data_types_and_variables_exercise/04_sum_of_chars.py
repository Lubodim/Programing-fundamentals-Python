number = int(input())
total_sum = 0
for char in range(number):
    ch = input()
    total_sum += ord(ch)
print(f"The sum equals: {total_sum}")
