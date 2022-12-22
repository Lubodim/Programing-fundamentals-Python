money = input().split(", ")
beggars = int(input())

sum_beggars = []
start_index = 0
money_digit = []
for cash in money:
    money_digit.append(int(cash))

while start_index < beggars:
    current_beggar_money = 0
    for collected_money in range(start_index, len(money_digit), beggars):
        current_beggar_money += money_digit[collected_money]
    sum_beggars.append(current_beggar_money)
    start_index += 1
print(sum_beggars)
