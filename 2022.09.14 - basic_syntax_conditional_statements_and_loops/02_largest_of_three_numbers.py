num_one = int(input())
num_two = int(input())
num_three = int(input())
largest_num = 0

if num_one > num_two and num_one > num_three:
    print(num_one)
elif num_two > num_three and num_two > num_one:
    print(num_two)
else:
    print(num_three)
