from pprint import pprint

BOARD_SIZE = 5
player_board = []
computer_board = []





def get_username():
    """
    Gets the username
    """
    user = input('Enter your username: ')
    print(f'Welcome to the battle of the ships {user}!')
    return username




user_choice = ""

def new_game():
    """
    Prints start game/instructions message and validates input for game to start.
    """
    user_choice = input("Type 'p' to start game or 'r' to read the rules!\n>")
    if user_choice == "r":
        display_instructions()
    elif user_choice == "p":
        set_board(hit,miss,comp)

def display_instructions():
    """
    Prints instructions to the screen for the user when "r" is selected.
    """
    print("These are the rules of my game")




def set_board(hit,miss,comp):
    """
    Prints X- axis as 1-5 and Y-axis as A-E

    """
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if  place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "

            row = row + ch
            place = place + 1
        print(x," ",row)
   
hit = [21,22]
miss = [20,24,12,13]
comp = [23] 

new_game()