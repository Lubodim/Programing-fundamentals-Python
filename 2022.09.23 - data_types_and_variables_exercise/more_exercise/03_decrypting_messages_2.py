key_word = int(input())
number_lines = int(input())
my_list = list()
for follow_str in range(number_lines):
    string = input()
    str_ascii = ord(string)
    my_list.append(chr(str_ascii + key_word))
print(my_list)