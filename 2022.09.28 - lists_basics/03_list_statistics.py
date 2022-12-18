number_of_numbers = int(input())

list_positive_numbers = []
list_negative_numbers = []

for _ in range(number_of_numbers):
    current_number = int(input())
    if current_number < 0:
        list_negative_numbers.append(current_number)
    else:
        list_positive_numbers.append(current_number)

print(list_positive_numbers)
print(list_negative_numbers)
print(f"Count of positives: {len(list_positive_numbers)}\nSum of negatives: {sum(list_negative_numbers)}")
