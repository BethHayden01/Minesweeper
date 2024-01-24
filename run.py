import random
import os


def main():
    """ Welcome message displayed to the user """
    print(f"""
Welcome to Minesweeper!

Instructions:

To begin, enter your desired number of single cell mines.

When prompted, enter a single number, from 0 to 5, 
to determine which row to place
your marker.

When prompted, enter a single number, from 0 to 5, 
to determine which column to place your marker

If you have hit a mine, your grid will display 
a M in the space you have chosen. 

If you have not hit a mine, the grid will display an X
in your chosen space.

If you hit all the mines,  the game will end, you have. 
Or if you chooose all the spaces without a mine, you win!
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
    if len(mines) > 10 or len(mines) < 1:
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
        for row in range(0,5):
            for col in range(0,5):
                if col ==4:
                    print(board[row][col])
                else:
                    print(board[row][col], end = " ")
        print('\n')


    def display_user_board():
        print("-"*21)
        for row in range(0,5):
            print("| ", end = "")
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
            col_str = input("Enter number for desired column position:")
            if col_str.isdigit() and int(col_str) in range(0,6):
                print("Input Valid")
                return int(col_str)
            else:
              print("That is not a number or is not 1 number long, try again.")


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
              print("That is not a number or is not 1 number long, try again.")

#places user guess and checks if the user has already guessed the cell 

    def user_placement():
        nonlocal num_mines_hit
        col = input_col()
        row = input_row()
        print(user_board[row][col])
        if user_board[row][col] == 'X' or user_board[row][col] == 'M':
            print(user_board[row])
            print("You have already hit this space, try again.")
        elif board[row][col] == 1:
            user_board[row][col] = 'M'
            print("You have hit a mine! Line 117")
            num_mines_hit += 1
        else:
            user_board[row][col] = 'X'
            print("You did not hit a mine! Congratulations")
            
    
    while num_mines_hit < mines:
        col = int(input_col())
        row = int(input_row())

        if user_board[row][col] == 'X' or board[row][col] == 'M':
            print("You have already hit this space, try again.")
        else:
            if user_board[row][col] == 1:
                user_board[row][col] = 'M'
                print ("You have hit a mine! Line 143")
                num_mines_hit += 1
            else:
                user_board[row][col] = 'X'
                print("You did not hit a mine! Congratulations")

        display_user_board()

#ends game if user has hit all mines
    def game_over():
        if num_mines_hit == mines: 
            print("GAME OVER! You have hit all the mines")
            return True
        else:
            return False

#ends the game if the user has guessed all spaces and not hit a mine.
    def game_win():
        if user_placement == 25 - [mines]:
            print("You have completed the game without hitting all the mines. You Win! Congratulations")
            return True
        else:
            return False

    user_placement()
    game_over()
    game_win()


main()

#label = list('12345')
        #for [row][col] in range(0,5):
            #print(label[i], end = " ")
            #print('\n')