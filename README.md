# rock-paper-scissors-exercise
This is my first attempt at writing my own python language to create a simple player-computer game of rock, paper, scissors. I walk you through how to set this game up below.

# Step 1: set up a new repo
In GitHub, create a new repo and name it "rock-paper-scissors-exercise", including a README.md file and a Python-flavored .gitignore file during the creation process.

Download the new repo to GitHub Desktop, cloning it to your computer - pay attention to where it's being saved!

In Git Bash, use the command-line to navigate to this repo on your drive (note you may need to update the following based on where you saved the repo on your drive):

```
cd ~\desktop\GitHub\rock-paper-scissors-exercise
```

In Visual Studio Code, add a new file and name it "game.py". Type the following:
# this is the "game.py" file...
print("Rock, Paper, Scissors, Shoot!")
Save


# step 2: set up the environment
Create and activate a new project-specific Anaconda virtual environment from the command-line:

```sh
conda create -n my-game-env python=3.8
conda activate my-game-env
```

From within this new environment, test running the Python script from the command-line:
```sh
python game.py
```

If you see the "Rock, Paper, Scissors, Shoot!" message, things have been set up correctly.

There is no pip install required for this game.


# step 3: input the code for the game
This is a standard game of rock-paper-scissors. The player needs to choose either rock, paper or scissors and then the computer will also choose one of those three options. If they pick the same option, it's a tie. Otherwise, rock beats scissors, paper beats rock, and scissors beat paper.

You will see in the game.py file that there is code to process the player's input, which standardizes the input to lowercase and let's the user know if there input is invalid.

You will also see in the game.py file that there is code to process the computer's selection using the choice() function provided by the random module. Note that in order to simulate random computer selection in our game, you must first import the random module. You will see this near the top of my game.py file as:

import random


You will also see in the game.py file that there is code to determine the outcome of the game.

Copy the code from my game.py file into yours and save.

*Note that there are many ways to write this code to achieve the same game experience. You should feel free to play around with other strategies for executing the code in this game.


# step 5: play the game
from the command-line, run the python script:

```
python game.py
```

Then follow the instructions to play a few games. You can try inputting invalid selections to see if it generates the expected response.

I hope you enjoyed setting up this simple game of rock, paper, scissors!