import random
import winsound
from termcolor import colored
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
win_player_counter = 0
win_computer_counter = 0

print("*********************************************************************************")

print("*******************************      Hello !!!     *****************************")

print("*********************  This is the Rock-Paper-Scissors Game  ********************")

print("*********************************************************************************")
print()

player_name = input("Please write your name here:")
print()
print(f"Hello {player_name} Today you will play against your computer!")
print()

while True:
    print()
    print(colored("The game will continue while one of you succeed to make 6 points", 'green'))
    print()
    print(colored(f"Your\'s POINTS {win_player_counter}  /  Computer\'s POINTS {win_computer_counter}", 'red'))
    if win_player_counter >= 6:
        print("Game Is Over - You win the game")
        break
    if win_computer_counter >= 6:
        print("Game Over")
        break
    print()
    print("         Enjoy the melody, while loading the GAME BEGIN !!!")
    print()
    for i in range(200, 2400, 200):
        winsound.Beep(i, 300)
    for i in range(2200, 200, - 200):
        winsound.Beep(i, 300)

    player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try to play the game again...")
    print(f"Your chose is {player_move}", end="  /  ")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    print(f"Computer chose is {computer_move}")
    print()

    if (player_move == rock and computer_move == scissors) or \
            (player_move == scissors and computer_move == paper) or \
            (player_move == paper and computer_move == rock):
        print("Congratulations you WIN and ADD 2 point in to your's account")
        win_player_counter += 2
    elif player_move == computer_move:
        print("Draw! - each of you lose 1 point")
        win_player_counter -= 1
        win_computer_counter -= 1
    else:
        print("You are a looser - Computer add 2 point in to his account")
        win_computer_counter += 2
