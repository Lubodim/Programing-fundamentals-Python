line_1 = input().split(" ")
line_2 = input().split(" ")
line_3 = input().split(" ")
winner = None
if line_1.count("1") == 3 or line_2.count("1") == 3 or line_3.count("1") == 3:
    winner = "First player won"
elif line_1.count("2") == 3 or line_2.count("2") == 3 or line_3.count("2") == 3:
    winner = "Second player won"
for index in range(len(line_2)):
    if line_1[index] == line_2[index] == line_3[index] == "1":
        winner = "First player won"
    elif line_1[index] == line_2[index] == line_3[index] == "2":
        winner = "Second player won"
if line_1[0] == line_2[1] == line_3[2] == "1":
    winner = "First player won"
elif line_1[0] == line_2[1] == line_3[2] == "2":
    winner = "Second player won"
if line_1[2] == line_2[1] == line_3[0] == "1":
    winner = "First player won"
elif line_1[2] == line_2[1] == line_3[0] == "2":
    winner = "Second player won"
if not winner:
    print("Draw!")
else:
    print(winner)
