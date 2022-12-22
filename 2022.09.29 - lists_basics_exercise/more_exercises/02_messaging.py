number_list = input().split(" ")
txt = list(input())
new_list = []
for word in number_list:
    digit_sum = 0
    for index, digit in enumerate(word):
        digit_sum += int(digit)
        for char in range(len(txt)):
            if digit_sum >= len(txt):
                digit_sum -= len(txt)
    new_list.append(txt[digit_sum])
    txt.pop(digit_sum)
for ch in new_list:
    print(ch, end="")

