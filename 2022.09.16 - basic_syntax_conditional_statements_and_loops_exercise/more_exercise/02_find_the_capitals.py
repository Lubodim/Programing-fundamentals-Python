word = input()
word_list = []
for index, digit in enumerate(word):
    if digit.isupper():
        word_list.append(index)
print(word_list)
