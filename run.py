import random
import os


def main():
    """ Welcome message displayed to the user """
    print(f"""
Welcome to Minesweeper!

Instructions:

To begin, enter your desired number of single cell mines.


When prompted, enter a single number, from 0 to 5,
to determine which column to place your marker.
Columns are numbered 1-5 horizontally.


When prompted, enter a single number, from 0 to 5,
to determine which row to place
your marker. Rows are numbered 1-5 vertically.


If you have hit a mine, your grid will display
a M in the space you have chosen and it is GAME OVER.


If you have not hit a mine, the grid will display an X
in your chosen space.

Happy Gaming!

    """)


    user_board = [[-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1]]


    mines = input("Enter the number of mines you desire: ")
    if mines.isdigit() and int(mines) in range(1, 11):
        print("Input valid.")
        mines = int(mines)
    else:
        print("That is not one number from 1 - 10. Try again.")
        while not mines.isdigit() or not int(mines) in range(1, 11):
            mines = input("Enter the number of mines you desire: ")
            if mines.isdigit() and int(mines) in range(1, 11):
                print("Input Valid.")
                mines = int(mines)
                break


    def display_user_board():
        print("-" * 21)
        for row in range(0, 5):
            print("| ", end="")
            for col in range(0, 5):
                if user_board[row][col] == -1:
                    print(" ", end=" | ")
                elif (user_board[row][col] == 'X' or
                      user_board[row][col] == 'M'):
                    print(user_board[row][col], end=" | ")
                else:
                    print(" ", end=" | ")
            print("")
            print("-" * 21)
    display_user_board()
    num_mines_hit = 0


    num = 0
    while num < mines:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if user_board[row][col] == -1:
            user_board[row][col] = 1
            num = num + 1


    def input_col():
        """ User enter column value"""
        while True:
            print(f"""
            Choose which column to place your mark.
            Input must be a single number ONLY.
            """)
            col_str = input("Enter number for desired column position:")
            if col_str.isdigit() and int(col_str) in range(1, 6):
                print("Input Valid")
                return int(col_str)-1
            else:
                print("That is not a number or is not 1 number, try again.")


    def input_row():
        """ User enter row value"""
        while True:
            print(f"""
            Choose which row to place your mark.
            Input must be a single number ONLY between 1 and 5.
            """)
            row_int = input("Enter number for desired row position:")
            if row_int.isdigit() and int(row_int) in range(1, 6):
                print("Input Valid")
                return int(row_int)-1
            else:
                print("That is not a number or is not 1 number, try again.")


    def user_placement():
        nonlocal num_mines_hit
        col = input_col()
        row = input_row()
        game_win = None

    mines = int(mines)
    while num_mines_hit < mines:
        col = int(input_col())
        row = int(input_row())
        if user_board[row][col] == 'X' or user_board[row][col] == 'M':
            print("You have already hit this space, try again.")
        else:
            if user_board[row][col] == 1:
                user_board[row][col] = 'M'
                print("You have hit a mine! GAME OVER")
                game_win = False
                display_user_board()
                break
            else:
                user_board[row][col] = 'X'
                print("You did not hit a mine! Input next guess.")
                game_win = True

        display_user_board()

    return game_win
    user_placement()


main()
