
race_times = input().split(" ")
left_racer = []
right_racer = []
race_lenth = (len(race_times) // 2)
index = 0
minus_index = -1
while race_lenth > index:
    left_racer.append(int(race_times[index]))
    right_racer.append(int(race_times[minus_index]))
    index +=1
    minus_index += -1

left_racer_sum = 0
right_racer_sum = 0
for final in range(len(left_racer)):
    left_racer_sum += left_racer[final]
    if left_racer[final] == 0:
        left_racer_sum *= 0.8
    right_racer_sum += right_racer[final]
    if right_racer[final] == 0:
        right_racer_sum *= 0.8
if left_racer_sum < right_racer_sum:
    print(f"The winner is left with total time: {left_racer_sum:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_sum:.1f}")
