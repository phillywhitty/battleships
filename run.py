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
        elif num % 9 == 0 and i < len(boat) - 1:
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
    taken = []
    ships = []
    boats = [5,4,3,3,2,2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1,4)
            print(b,boat_start,boat_direction)
            boat = check_boat(b,boat_start,boat_direction,taken)
        ships.append(boat)
        taken = taken + boat
        print(ships)

    return ships,taken


def get_shot(guesses):

    ok = "n"
    while ok =="n":
        try:
            shot = input("please enter your guess")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number, please try again")
            elif shot in guesses:  
                print("incorrect number, used before")  
            else:
                ok = "y"
                break 
        except:
            print("incorrect entry - please enter again")

    return shot



def show_board(taken):

    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if  place in taken:
                ch = " x "
            row = row + ch
            place = place + 1
        print(x," ",row)

boats,taken = create_boats()
show_board(taken)        
   

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
