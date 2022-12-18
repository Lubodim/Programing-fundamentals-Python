number_of_strings = int(input())
given_word = input()
string_list = []

for _ in range(number_of_strings):
    current_string = input()
    string_list.append(current_string)

print(string_list)

for word in range(len(string_list) - 1, -1, -1):
    part_of_list = string_list[word]
    if given_word not in part_of_list:
        string_list.remove(part_of_list)

print(string_list)
