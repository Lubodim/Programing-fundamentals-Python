first_number = int(input())
second_number = int(input())
ascii_string = ""
for asci in range(first_number, second_number +1):
    ascii_string += chr(asci) + " "
print(ascii_string)
