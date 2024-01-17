import random

board = [0,0,0,0,0], 
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]


mines = int(input("Enter the number of mines you desire"))
if mines > 25:
    print("Too many mines. Set to 5")
    mines=5
num=0
while num < mines:
    row=random.randint(0,4)
    col=random.randint(0,4)
    if board[row][column]==0:
        board[row][column]=1
        num=num+1

def display_board():
    for row in range (0,5):
        for col in range (0,5):
            print(board[row][col], end = " ")

display_board()



def main():
    """
    Welcome message displayed to the user
    """ 
    print("Welcome to Minesweeper! Hit enter to start\n")
    print("Instructions:\n")
    print("1. When prompted, enter a single letter to determine which row to place your marker")
    print("2. When prompted, enter a single number to determine which column to place your marker\n")
    print("If you have hit a mine, your marker will display a *, if not your marker will display an X")
        

def validate_row(values):
    """
    Validates if the user has input either an int
    for the row input. Validates Length.
    """
    value = input("Enter a value: ")
    if isinstance(value, int) and len(value) == 1:
        print("Value accepted")
        else:
            print("The value is not a number or is not exactly 1 letter long. Please try again.")
                
        
def validate_column(values):
    """
    Validates if the user has input either a str 
    for the column input. Validates Length.
    """
    value = input("Enter a value: ")
    if isinstance(value, str) and len(value) == 1:
        print("The value is a string and is exactly 1 letter long.")
    else:
        print("The value is not a string or is not exactly 1 letter long. Please try again.")



main()
        
