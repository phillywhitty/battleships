from random import randrange


def check_ok(boat,taken):

    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat) - 1:
            if boat[i+1] % 10 == 0:  
                boat = [-1]
            break

    return boat    



def check_boat(b,start,dirn,taken):

    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_ok(boat,taken)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
            boat = check_ok(boat,taken)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
            boat = check_ok(boat,taken)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
            boat = check_ok(boat,taken)
    return boat        

   
def create_boats(): 
    """
    Iterates over each boat size in the boat list
    Creates a placeholder [-1] which enters a while loop until a valid postion is found.
    It generates a starting postion and also a direction.
    When returned boat is valid it adds to the list of ships
    """ 
    taken = []
    ships = []
    # Boat Sizes
    boats = [5,4,3,3,2,2]
    for b in boats:
        # Placeholder
        boat = [-1]
        while boat[0] == -1:
            # Generates random starting position    
            boat_start = randrange(99)
            # Generates random direction (1: up, 2: right, 3: down, 4: left)    
            boat_direction = randrange(1,4)
            print(b,boat_start,boat_direction)
            # Checks to see if boat postion is valid
            boat = check_boat(b,boat_start,boat_direction,taken)
        # Adds valid boat to list of ships    
        ships.append(boat)
        taken = taken + boat
        print(ships)
    # Returns list of ships and taken places
    return ships,taken


def get_shot_computer(guesses):

    """
    Retrieves the users shots and validates them.
    Storing the guess into the shot variable we convert it into an integer.
    Checks to see if shots are within valid range or guessed before.
    When guess is valid we break from loop returning the shot
    """

    ok = "n"
    while ok =="n":
        try:
            shot = randrange(99)
        
            # Checks to see if shot is in already guessed list
            if shot not in guesses:  
                ok = "y"
                guesses.append(shot)
                break 
            # An exception if users types non-numeric value    
        except:
            print("incorrect entry - please enter again")

    return shot, guesses

def show_board(hit,miss,comp):
    print("            battleships    ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x " 
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "   
            row = row + ch
            place = place + 1
            
        print(x," ",row)       

def check_shot(shot,ships,hit,miss,comp):
    missed = 1
    for i in range(len(ships)):

        if shot in ships[i]:
            ships[i].remove(shot)
            missed = 0
            if len(ships[i]) > 0:
                hit.append(shot)
            else:
                comp.append(shot)      

    if missed == 1:
        miss.append(miss)

           
    return ships,hit,miss,comp
    

hit = []
miss = []
comp = []
guesses = []
ships,taken = create_boats()
show_board_c(taken) 

for i in range(2):
    shot,guesses = get_shot_computer(guesses)
    ships,hit,miss,comp = check_shot(shot,ships,hit,miss,comp)
    show_board(hit, miss, comp)

def show_board_c(taken):

    """
    Sets the starting place num to 0. Code then loops through each row
    of the board creating an empthy string to store the row.
    Then the loop inside runs through the columns setting my characters to " _ ".
    It then checks my taken list and sets characters to " x " if taken.
    """

    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    # Loops through rows
    for x in range(10):
        row = ""
        # Loops through columns
        for y in range(10):
            ch = " _ "
            # Checks my taken list
            if  place in taken:
                ch = " o "
            row = row + ch
            # Increase place number by 1 for each Iteration
            place = place + 1
        print(x," ",row)



def check_shot(shot,boat1,boat2,hit,miss,comp):

    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)      
    elif shot in boat2:
        boat2.remove(shot)
        if len(boat2) > 0:
            hit.append(shot)
        else:
            comp.append(shot)    

    else:
        miss.append(shot) 


    return boat1,boat2,hit,miss,comp
 

boat1 = [45,46,47]   
boat2 = [6,16,26]
hit = []
miss = []
comp = [] 

for i in range(10):
    guesses = hit + miss + comp
    shot = get_shot(guesses)
    boat1,boat2,hit,miss,comp = check_shot(shot,boat1,boat2,hit,miss,comp)
    show_board(hit,miss,comp)

    if len(boat1) < 1 and len(boat2) < 1:
        print('you have won')

print("finished")        
