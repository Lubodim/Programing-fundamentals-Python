numbers = input().split()
numbers_to_remove = int(input())
numbers_as_digit = []

for num in numbers:
    numbers_as_digit.append(int(num))

for _ in range(numbers_to_remove):
    numbers_as_digit.remove(min(numbers_as_digit))
for digit in numbers_as_digit:
    if digit != numbers_as_digit[-1]:
        print(digit, end=", ")
    if digit == numbers_as_digit[-1]:
        print(digit)
