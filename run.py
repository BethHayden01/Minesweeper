import random
import os


board = [[0,0,0,0,0], 
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]


def display_board():
    for row in range (0,5):
        for col in range (0,5):
            print(board[row][col], end = " ")


def main():
    """ Welcome message displayed to the user """ 
    print(f"""
Welcome to Minesweeper! Hit enter to start

Instructions:

1. When prompted, enter a single letter to determine which row to place
your marker
2. When prompted, enter a single number to determine which column to place your marker

If you have hit a mine, your marker will display a *, if not your marker will display an X
    """)
    # while mines is not int or len(mines) > 10 or len(mines) < 1 please repeat input
    mines = input("Enter the number of mines you desire: ")
    if len(mines) > 10 and len(mines) < 1:
        print("Use one number from 1 - 10")
    try :

        mines = int(mines)
        num=0
        print("test1")
        while num < mines:
            print("test2")
            row=random.randint(0,4)
            col=random.randint(0,4)
            if board[row][col]==0:
                board[row][col]=1
                num=num+1
        display_board()
    except ValueError:
        print("Use ONLY one number from 1 - 10")


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
                


def display_board():
    for row in range (0,5):
        for col in range (0,5):
            if col ==4:
                print(board[row][col])
            else:
                print(board[row][col], end = " ")
    print('\n')

display_board()
        

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
        
