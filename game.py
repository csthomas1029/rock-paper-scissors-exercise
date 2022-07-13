# this is the "game.py" file...
# inspiration for code language from https://nyu-tech-2335.slack.com/archives/C5WPFSB52
import random
# this imports the random module which we need for the computer selection

print("Rock, Paper, Scissors, Shoot!")


# USER INPUTS
player_choice = input("Welcome! Please make a selection ('rock', 'paper', 'scissors'): ")
player_choice = player_choice.lower()
# this way every time we use the player_choice it will be lowercase

print("You chose:", player_choice)


# VALIDATE USER INPUTS
valid_choices = ["rock", "paper", "scissors"]

if player_choice not in valid_choices:
    print("Invalid. Please ensure you make a valid selection.")
    exit()
# this way the game ends with a logical message if the player puts in an invalid selection


# SIMULATE COMPUTER SELECTION
computer_choice = random.choice(valid_choices)
print("Computer chose:", computer_choice)


# DETERMINE THE WINNER
if player_choice == computer_choice:
    print("You both chose ", player_choice,". It's a tie!")
elif player_choice == "rock" and computer_choice == "paper":
    print("Oh, the computer won. It's ok.")
elif player_choice == "rock" and computer_choice == "scissors":
    print("Congrats! You beat the computer.")
elif player_choice == "paper" and computer_choice == "rock":
    print("Congrats! You beat the computer.")
elif player_choice == "paper" and computer_choice == "scissors":
    print("Oh, the computer won. It's ok.")
elif player_choice == "scissors" and computer_choice == "rock":
    print("Oh, the computer won. It's ok.")
elif player_choice == "scissors" and computer_choice == "paper":
    print("Congrats! You beat the computer.")
else:
    exit()


# DISPLAY THE RESULTS
print("Thanks for playing and please come play again!")