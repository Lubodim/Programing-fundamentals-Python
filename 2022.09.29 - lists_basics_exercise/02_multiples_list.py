factor = int(input())
count = int(input())

int_list = []
for num in range(1, count + 1):
    int_list.append(num * factor)
print(int_list)