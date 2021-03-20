# Brida app
## still developing
Brida app is a digital version of the popular board game party alias.

## Python and Kivy
Python version used: Python 3.6.9
Kivy version used: Kivy 2.0.0

# Instructions - before launching app

## same folder for py and kv files
In order to be able to launch the app you have to download the python file (brida.py), kivy (birda.kv) and list of word names file (word_lst_en.txt) file and put them in the same folder.

## copy full full path
open the brida.py and replace the full path ("C:\\Users\\AT\\Documents\\git_projects\\brida-app\\brida.py") with your full path of the word_lst_en.txt

## Game concept
### Players
Minimum of 4 players required, supports up to 10 players. Number of players in a team must be even, which means that up to 5 teams of 2 players can play the game.

### Random word
A random word is generated from a word list.
### Game play
Player 1 explains a random word to player 2. Whenever the team gets a word right, the player explaining a word types in “correct” and the next word comes out. The team needs to guess as many words as possible within a minute. Teams earn +1 point for each correctly guessed word and lose -1 point by skipping unfamiliar words. If teams use Joker, they can skip a word without losing a point.

### Winner
After each round the winner is evaluated. Winner is the team which first wins 10 points.

## TO DO
Exit round when time runs out.

## TO DO 2 DATA SCIENCE & AI
- Collect data based on  names,  time when the game is played,  time spent on guessing a specific word etc.

- Create AI to make different lists of words, based on word difficulty level.

# please contact me if you want to collaborate

