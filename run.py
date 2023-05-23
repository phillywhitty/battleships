from random import randrange
import random

def check_ok(boat,taken):

    boat.sort()
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
        if i != 0:
            if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                boat = [-1]
                break
    return boat  

def get_ship(long,taken):
    
    ok = True
    while ok:
        ship = []
        #ask the user to enter numbers
        print("enter your ship of lenght ",long)
        for i in range(long):
            boat_num = input("please enter a number")
            ship.append(int(boat_num))
        #check that ship
        ship = check_ok(ship,taken)
        if ship[0] != -1:
            taken = taken + ship
            break
        else:
            print("error - please try again")    

    return ship

def create_ships():
    taken = []
    ships = []
    boats = [5,4,3,3,2,2]

    for boat in boats:
        ship = get_ship(boat,taken)
        ships.append(ship)

    return ships

ships = create_ships()


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
           
            # Checks to see if boat postion is valid
            boat = check_boat(b,boat_start,boat_direction,taken)
        # Adds valid boat to list of ships    
        ships.append(boat)
        taken = taken + boat
  
    # Returns list of ships and taken places
    return ships,taken


def get_shot_computer(guesses,tactics):

    """
    Retrieves the users shots and validates them.
    Storing the guess into the shot variable we convert it into an integer.
    Checks to see if shots are within valid range or guessed before.
    When guess is valid we break from loop returning the shot
    """

    ok = "n"
    while ok =="n":
        try:
            if len(tactics) > 0:
                shot = tactics[0]
            else:    
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



def check_shot(shot,ships,hit,miss,comp):
    missed = 0
    for i in range(len(ships)):

        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                comp.append(shot)      
                missed = 2
    if missed == 0:
        miss.append(miss)

           
    return ships,hit,miss,comp, missed
    
def calc_tactics(shot,tactics,guesses,hit):


    if len(tactics) < 1:
        temp = [shot-1,shot+1,shot-10,shot+10]
    else:
        if shot-1 in hit: 
            if shot -2 in hit:
                temp = [shot-3,shot+1]
            else:
                temp = [shot-2,shot+1]  
        elif shot+1 in hit: 
            if shot -2 in hit:
                temp = [shot+3,shot-1]
            else:
                temp = [shot+2,shot-1]  
        elif shot-10 in hit: 
            if shot -2 in hit:
                temp = [shot-30,shot+10]
            else:
                temp = [shot-20,shot+10]   
        elif shot+10 in hit:
            if shot -2 in hit:
                temp = [shot+30,shot-10]
            else:
                temp = [shot+20,shot-10] 
             
    #tactics longer
    cand = []
    for i in range (len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
    random.shuffle(cand)       

    return cand         

def check_if_empty_2(list_of_lists):
    return all([not elem for elem in list_of_lists ])

hit = []
miss = []
comp = []
guesses = []
ships,taken = create_boats()

tactics = []

for i in range(80):
    shot,guesses = get_shot_computer(guesses, tactics)
    ships,hit,miss,comp,missed = check_shot(shot,ships,hit,miss,comp)

    if missed == 1:
        tactics = calc_tactics(shot,tactics,guesses,hit)
    elif missed == 2: 
        tactics = []
    elif len(tactics) > 0:
        tactics.pop(0) 

    if check_if_empty_2(ships):
        print("end of game",i)   
        break   

show_board_c(taken)
show_board(hit, miss, comp)


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
    shot = get_shot_computer(guesses,tactics)
    boat1,boat2,hit,miss,comp = check_shot(shot,boat1,boat2,hit,miss,comp)
    show_board(hit,miss,comp)

    if len(boat1) < 1 and len(boat2) < 1:
        print('you have won')

print("finished")        
