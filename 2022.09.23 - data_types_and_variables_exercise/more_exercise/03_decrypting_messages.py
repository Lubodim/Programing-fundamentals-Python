key_word = int(input())
number_lines = int(input())
for follow_str in range(number_lines):
    string = input()
    str_ascii = ord(string)
    print(chr(str_ascii + key_word), end="")
