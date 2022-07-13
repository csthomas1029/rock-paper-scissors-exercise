# this is the "game.py" file...
import random

print("Rock, Paper, Scissors, Shoot!")



# USER INPUTS
player_choice = input("Welcome! Please make a selection ('rock', 'paper', 'scissors'): ")
player_choice = player_choice.lower()

print("You chose:", player_choice)


# VALIDATE USER INPUTS


# SIMULATE COMPUTER SELECTION
valid_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_choices)
print("Computer chose:", computer_choice)

# DETERMINE THE WINNER
# inspiration for code language from https://nyu-tech-2335.slack.com/archives/C5WPFSB52
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
    print("Invalid. Please note that the selections are case sensitive.")


# DISPLAY THE RESULTS


# -------------------
# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!
