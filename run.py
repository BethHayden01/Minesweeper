import string



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
        
