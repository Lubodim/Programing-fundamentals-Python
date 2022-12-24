def rounding(lis):
    new_lis = []
    for char in lis:
        current_num = float(char)
        new_lis.append(round(current_num))
    return new_lis


my_list = input().split(" ")

print(rounding(my_list))