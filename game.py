# this is the "game.py" file...
import random

print("Rock, Paper, Scissors, Shoot!")



# USER INPUTS
player_choice = input("Welcome! Please make a selection ('rock', 'paper', 'scissors'): ")

print("You chose:", player_choice)


# VALIDATE USER INPUTS


# SIMULATE COMPUTER SELECTION
valid_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_choices)
print("Computer chose:", computer_choice)

# DETERMINE THE WINNER


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
