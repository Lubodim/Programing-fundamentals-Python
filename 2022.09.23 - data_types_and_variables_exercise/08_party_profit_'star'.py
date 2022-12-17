group_size = int(input())
days = int(input())
coins = 0
companions_count = group_size
for day_mining in range(1, days + 1):
    if day_mining % 10 == 0:
        companions_count -= 2
    if day_mining % 15 == 0:
        companions_count += 5
    coins += 50
    coins -= companions_count * 2  # food for companion
    if day_mining % 3 == 0:
        coins -= companions_count * 3  # diner motivational party for companion
    if day_mining % 5 == 0:
        coins += 20 * companions_count  # slay a boss monster
        if day_mining % 3 == 0:
            coins -= 2 * companions_count  # diner motivational party for companion
print(f"{companions_count} companions received {int(coins / companions_count)} coins each.")