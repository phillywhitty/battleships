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
        set_board()

def display_instructions():
    """
    Prints instructions to the screen for the user when "r" is selected.
    """
    print("These are the rules of my game")




def set_board():
    """
    Prints X- axis as 1-5 and Y-axis as A-E

    """
    print(f"{username}'s Fleet")
    print(f'    1 2 3 4 5')
    print('---------------')
    

new_game()