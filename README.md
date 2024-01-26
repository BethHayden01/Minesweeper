# MineSweeper Game

*The link to [Minesweeper](https://minesweeper-4f4b.onrender.com/)

This Minesweeper game, coded in Python, creates a terminal in which users can interact to initiate and complete a game of Minesweeper. 

The rules of the game are displayed upon inititation to provide the user with a detailed explanation of how the game runs and how their interactions generate the desired response. 

## Playing the game: 
1. click the link provided to open the game. 
2. Read through the instructions provided to gain knowledge of how the game runs and the rules of the game.
3. Enter the desired number of randomly placed mines on the board.
4. Study the board and enter the desired column placement.
5. Enter the desired row placement corresponding to the previously entered column selection.
6. Recive feedback as to whether or not a mine has been hit.
7. Continue entering column and row placements until a mine has been hit.
8. Recive a message informing you of the outcome.
9. Once a mine has been hit, the program will end. 

## User Stories 

### First time user goals
- As a first time user I need to be able to access the game quickly and efficiently. 
- As a first time use I need tobe able to easily locate the intructions and rules on how to play the game. 
- As a fist time user I need to be able to follow along with the game without feeling lost. 
- As a first time user I need feedback as to my progress on locating the mines. 

### Multiple visit user goals: 
- As a returning user, I need to be able to refresh myself on the rules and instrictions of the game. 
- As a returning user, I need to be able to change the value of mines on the board so the game does not get boring.
- As a returning user, I need the location of the mines to change from the last time I played. 

## Features

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

## Flowchart

The below flowchart outlines the logic algorithm of the game and how to continues until the end.
(Screenshot)

## Technologies used

The languages used throughout this game were: 
- Python 3.8.5
- Javascript
- HTML

The python imports used in this game are:
- random is used to randomly generate the mines on the user board.
- os 

other tools used when geenrating this game were: 
- CodeAnywhere - Used as initial coding workspace before issues occured with the software. 
- GitPod - Used as final coding workspace.
- Git
- GitHub - Used for version tracking
- render.com - Used to deploy the terminal project.

## Bugs

Throughout the creation of this game many bugs were encountered. 

solved bugs: 
1. The first solved bug was a break in the flow of the code. The code did not run past the user column input. 
(Screenshot of broken code)
This was fixed by the addition of a break after the column input while loop.
(Screenshot)

2. The code used to detect if a mine had been hit only responded to integer inputs and therefore produced the following error message. 
(Screenshot)
This was fixed by altering the structure of my column input to request an integar rather than a string. 

3. Another bug that occured during the creation of my project was in realtion to mine generation. After initial user mine input and the first column+row selection, the program displayed the location of the mines to the user. 
(Screenshot)
This was fixed by expanding the elif statement within the display_user_board function to only print 'X' or 'M' on the board and not the 1 representing a mine.
(Screenshot)

## Unsolved bugs

The only unsolved bug I have found in my program is an issue on the Python PEP8 Linter. 

Because I chose to code all of my functions inside of my main, the linter produces a E303: Too many blank lines error on lines 37, 44, 58, 76, 85, 100 and 115.
However, this bug does not affect the flow of the program, in fact, when this bug is resolved, the program no longer runs. 
Therefore, I decided it to be beneficial to leave this issue alone as it is not directly affecting the flow of the program.

## Testing

The testing carried out on this project can be found in [TESTING.md](TESTING.md).

## Deployment

This terminal project is deployed on Render.com and ccan be reached on the following [link](https://minesweeper-4f4b.onrender.com/)

### Deployment to Render.com steps

In order to use Render you must first have an account. This is completley free to set up and use. 

Once that has been done you can begin setting up your terminal application. 

1. On your dashboard, select the large purple 'New+' button and select the 'Web Service' option on the drop down menu.
2. Now you will attach your GitHub repository to this web service by selecting 'Build and Deploy from a Git repository'.
3. You will now see a list of your repositories, make sure to select the correct one for your terminal application, then select 'Connect'.
4. To set up your terminal, input a name for the project, followed by the region in which it is to be hosted. In this case, I chose Europe.
5. Next, Select the branch of your code to deploy from. This will usually be your main. 
6. Now we can select the environment for our code, in this case it would be Python 3.
7. Then add the Build commands 'pip3 install -r requirements.txt && npm install.
8. Once that is done you can add the Start Command 'node index.js'
9. Make sure you choose the free plan to deploy your project.
10. Select the Advanced Settings at the bottom of the form and add the Environment variables as follows:
    Key: PORT               Value:8000
    key: PYTHON_VERSION     Value: 3.10.7
11. Then finally you can  select 'Create Web Service' at the base of the form. 

Once the deployment is complete, you can play your terminal game. 

## Credits

1. Credit to render.com for hosting the terminal application.
2. The Code Institute for providing a clear walkthrough of Python termial applications.

## Acknowledgements

1. [Iuliia-Konovalova](https://github.com/IuliiaKonovalova) my mentor helped me greatly through the creation of my project. 