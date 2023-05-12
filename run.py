from pprint import pprint

def username():
    """
    Gets the username
    """
    user = input('Enter your username: ')
    print(f'Welcome to the battle of the ships {user}!')


username()






user_choice = ""

def new_game():
    """
    Prints start game/instructions message and validates input for game to start.
    """
    user_choice = input("Type 'p' to start game or 'r' to read the rules!\n>")
    if user_choice == "r":
        display_instructions()
    elif user_choice == "p":
        print("set_board")   

def display_instructions():
    """
    Prints instructions to the screen for the user when "r" is selected.
    """
    print("These are the rules of my game")

new_game()