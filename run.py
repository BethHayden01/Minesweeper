import random
import os


def main():
    """ Welcome message displayed to the user """ 
    print(f"""
Welcome to Minesweeper! Hit enter to start

Instructions:

When prompted, enter a single letter to determine which row to place
your marker
When prompted, enter a single number to determine which column to place your marker

If you have hit a mine, your marker will display a , if not your marker will display an X
    """)
    #Board that the user should not see 
    board = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]


    #Board that the user should see 
    user_board = [[-1,-1,-1,-1,-1], 
        [-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1]]


    # while mines is not int or len(mines) > 10 or len(mines) < 1 please repeat input
    mines = input("Enter the number of mines you desire: ")
    if len(mines) > 10 and len(mines) < 1:
        print("Use one number from 1 - 10")
    try :
        mines = int(mines)
        num=0
        while num < mines:
            row=random.randint(0,4)
            col=random.randint(0,4)
            if board[row][col]==0:
                board[row][col]=1
                num=num+1
    except ValueError:
        print("Use ONLY one number from 1 - 10")

    def display_board():
        for row in range (0,5):
            for col in range (0,5):
                if col ==4:
                    print(board[row][col])
                else:
                    print(board[row][col], end = " ")
        print('\n')


    def display_user_board():
        print ("-"*21)
        for row in range (0,5):
            print ("| ", end = "")
            for col in range (0,5):
                if user_board[row][col] == -1:
                    print(" ",  end = " | ")
                else:
                    print(user_board[row][col], end = " | ")
            print("")
            print("-"*21)
    display_user_board()
    num_mines_hit = 0


    def input_col():
        """ User enter column value"""
        while True: 
            print(f"""
            Choose which column to place your mark. 
            Input must be a single number ONLY.
            """)
            col_str = input ("Enter number for desired column position:")
            if (col_str, str) and len(col_str) == 1:
                print("Input Valid")
                return int(col_str)
            else:
              print("The value is not a number or is not exactly 1 number long. Please try again.")


    def input_row():
        """ User enter row value"""
        while True: 
            print(f"""
                Next, choose which row you wish to place your mark.
                Count down the grid and input that number. 
                Input must be a single number ONLY. 
                """)
            row_int = input("Enter number for desired row postion:")

            if isinstance(row_int, str) and len(row_int) == 1:
                print("Value accepted")
                return int(row_int)
            else:
              print(len(row_int))
              print("The value is not a number or is not exactly 1 letter long. Please try again.")

    #places user guess and checks if the user has already guessed the cell 
    def user_placement(): 
        col = input_col()
        row = input_row()
        if user_board[row][col] == 'X' or user_board[row][col] == 'M':
            print("You have already hit this space, try again.") 
        elif board[row][col] == 1:
            user_board[row][col] = 'M'
            print ("You have hit a mine!")
            num_mines_hit += 1
        else:
            user_board[row][col] = 'X'
            print("You did not hit a mine! Congratulations")
            
    
    while num_mines_hit < mines:
        user_board = [[-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1]]

        display_user_board()
        
        col = int(input_col())
        row = int(input_row())

        if board[row][col] == 1:
            user_board[row][col] = 'M'
            print ("You have hit a mine!2")
            num_mines_hit += 1
        else: 
            user_board[row][col] = 'X'
            print("You did not hit a mine! Congratulations")
        
        display_user_board()        
        
    # ends game if user has hit all mines
    def game_over():
        if num_mines_hit == mines: 
            print("GAME OVER! You have hit all the mines")
            return True
        else:
            return False
        
    # ends the game if the user has guessed all spaces and not hit a mine.
    def game_win():
        if user_placement == 25 - mines:
            print("You have completed the game without hitting all the mines. You Win! Congratulations")
            return True
        else:
            return False
        
    user_placement()
    game_over()
    game_win()
        

main()