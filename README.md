# rock-paper-scissors-exercise
First attempt at writing my own python language for a game

Step 1: Set up a new repo in GitHub
Name it "rock-paper-scissors-exercise", add a README.md file and a Python-flavored .gitignore file during the creation process.
Download the new repo to GitHub Desktop, cloning it to my computer - pay attention to where it's being saved!

In Git Bash, use the command-line to navigate to this repo on my drive (cd ~[FILE LOCATION])

In Visual Studio Code, add a new file and name it "game.py". Type the following:
# this is the "game.py" file...
print("Rock, Paper, Scissors, Shoot!")
Save

Step 2: Set up the environment
Create and activate a new project-specific Anaconda virtual environment from the command-line:
conda create -n my-game-env python=3.8
conda activate my-game-env

From within this new environment, test running the Python script from the command-line:
python game.py

If you see the "Rock, Paper, Scissors, Shoot!" message, things have been set up correctly.