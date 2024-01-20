MineSweeper Game

This Minesweeper game, coded in Python, creates a terminal in which users can interact to initiate and complete a game of Minesweeper. 

The rules of the game are displayed upon inititation to provide the user with a detailed explanation of how the game runs and how their interactions generate the desired response. 

Playing the game: 
1. click the link provided to open the game. 
2. Read through the instructions provided to gain knowledge of how the game runs and the rules of the game.
3. Enter the desired number of randomly placed mines on the board 
4. Study the board and enter the desired column placement.
5. Enter the desired row placement corresponding to the previously entered column selection.
6. Recive feedback as to whether or not a mine has been hit.
7. Continue entering column and row placements until either all the mines have been hit, or the game is complete. 
8. Recive a message informing you of the outcome.
9. The program will then end. 

User Stories 

First time user goals
- As a first time user I need to be able to access the game quickly and efficiently. 
- As a first time use I need tobe able to easily locate the intructions and rules on how to play the game. 
- As a fist time user I need to be able to follow along with the game without feeling lost. 
- As a first time user I need feedback as to my progress on locating the mines. 

Multiple visit user goals: 
- As a returning user, I need to be able to refresh myself on the rules and instrictions of the game. 
- As a returning user, I need to be able to change the value of mines on the board so the game does not get boring.
- As a returning user, I need the location of the mines to change from the last time I played. 

Features

Upon start up of the game the user is met with a welcome messsage followed by the instructions and rules of the game as seen below:
(Screenshot of the start window)

Next the user is met with a message asking how many mines they wish the spawn onto the board.
(Screenshot)

After this the user is able to view the board.
(screenshot)

The user is then able to choose which column they wish to place their mine.
(screenshot)

Following this, the user can enter the row in which they wish to place this mine. 
(Screenshot)

The user can then see on the board if their placement has hit a mine or not through the feedback of an X for no hit or a * for a hit.
(Screenshot)

If the user has not hit a mine the game shall loop until either the game is complete and they have no more grid placements to choose, or all of the mines have been hit. 
Once this occurs, the user will be displayed with either a 'Game over' message following contact with all mines, or a 'congratulations' message if the cells have all been selected with no mine hits. 
(Screenshot)

Flowchart

The below flowchart outlines the logic algorithm of the game and how to continues until the end.
(Screenshot)

Technologies used

The languages used throughout this game were: 
- Python 3.8.5
- Javascript
- HTML

The python imports used in this game are:
- random 
- os 

other tools used when geenrating this game were: 
- CodeAnywhere
- Git
- GitHub
- render.com

Bugs

Throughout the creation of this game many bugs were encountered. 

solved bugs: 
1. The first solved bug was a break in the flow of the code. The code did not run past the user column input. 
(Screenshot of broken code)
This was fixed by the addition of a break after the column input while loop.
(Screenshot)

2. The code used to detect if a mine had been hit only responded to integer inputs and therefore produced the following error message. 
(Screenshot)
This was fixed by altering the structure of my column input to request an integar rather than a string. 