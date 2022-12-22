energy = 100
coins = 100
flag = True
event_day = input().split("|")
for event in event_day:
    action, num = event.split("-")
    num = int(num)
    if action == "rest":
        gained_energy = 0
        current_energy = energy + num
        if current_energy > 100:
            gained_energy = abs(100 + num - current_energy)
        else:
            energy = current_energy
            gained_energy = num
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif action == "order":
        energy -= 30
        if energy >= 0:
            print(f"You earned {num} coins.")
            coins += num
        else:
            energy += 30  # skip the order
            energy += 50  # take rest
            print("You had to rest!")
    else:
        if coins >= num:
            coins -= num
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            flag = False
            break
if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
