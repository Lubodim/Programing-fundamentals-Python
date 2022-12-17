budget = int(input())
money_for_spend = budget
is_buy_everything = True
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        is_buy_everything = False
        break
    command = int(command)
    money_for_spend -= command
    if money_for_spend < 0:
        print(f"You went in overdraft!")
        is_buy_everything = False
        break
if is_buy_everything:
    print("You bought everything needed.")
