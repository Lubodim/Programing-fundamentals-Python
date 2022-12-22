word_list = input().split(", ")
int_list = []
count_zero = word_list.count("0")
for word in word_list:
    if int(word) != 0:
        int_list.append(int(word))
for word in word_list:
    if int(word) == 0:
        int_list.append(int(word))
print(int_list)