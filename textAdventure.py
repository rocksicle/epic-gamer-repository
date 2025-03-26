'''
textAdventure.py
'''

import sys

def room1():
    room1_possibilites=["Enter left door", "Enter front door", "Search the room", "Laugh","Turn around", "Quit"]

    print("You awaken in a room. There is a dimly lit torch on a wall to your left side, but otherwise there is no lighting. There is a door in front of you as well as one to your left.\n")

    user_input=str(input("Enter left door, Enter front door, Search the room, Laugh, Turn around or Quit?\n "))

    while user_input!=room1_possibilites[5]:
        while user_input not in room1_possibilites:
            print("Not valid input. Make sure to type your input exactly the same as they are in the prompt!\n")
            user_input=str(input("Enter left door, Enter front door, Search the room, Laugh, or Quit?\n "))

        while user_input in room1_possibilites:
            if user_input==room1_possibilites[0]:
                room2()
            if user_input==room1_possibilites[1]:
                room3()
            if user_input==room1_possibilites[2]:
                CanOfPaint()
            if user_input==room1_possibilites[3]:
                print("You laugh, even though nothing is very funny. You die of oxygen overdose.\n")
                sys.exit("Ending Unlocked: Too much air")
                
            if user_input==room1_possibilites[4]:
                print("You turn around, and see a short, long haired figure right in front of you.")
                sys.exit("Ending Unlocked: Thats about it, see ya")
    if user_input=="Quit":
        sys.exit("Quitted")

def CanOfPaint():
    CanOfPaint_possibilites=["Consume beverage","Set it down","Quit"]
    print("You found a can of teal paint. The can is open, but the paint is still liquid.\n")
    user_input=input("Consume beverage, Set it down or Quit?\n")


    while user_input != CanOfPaint_possibilites[2]:
        while user_input not in CanOfPaint_possibilites:
            print("Not valid input. Make sure to type your input exactly the same as they are in the prompt!\n")
            user_input=input("Drink the paint, Set it down or Quit?\n")

        while user_input in CanOfPaint_possibilites:
            if user_input==CanOfPaint_possibilites[0]:
                print("You spill the paint everywhere. Your vision gets blurry, but it tastes sweet...\n ")
                room1()
            if user_input==CanOfPaint_possibilites[1]:
                print("You leave the paint be and go on your way\n")
                return

    if user_input=="Quit":
        sys.exit("Quitted")

def room2():
    room2_possibilites=["Drink the paint","Break down and cry", "Think of the cure for cancer", "Take a step forward","Go back", "Quit"]

    print("You enter a room filled with different colored paints. \n")

    user_input=str(input("Drink the paint, Break down and cry, Think of the cure for cancer, Take a step forward, Go back, or Quit?\n "))

    while user_input!=room2_possibilites[5]:
        while user_input not in room2_possibilites:
            print("Not valid input. Make sure to type your input exactly the same as they are in the prompt!\n")
            user_input=str(input("Enter left door, Enter front door, Search the room, Laugh, or Quit?\n "))

        while user_input in room2_possibilites:
            if user_input==room2_possibilites[0]:
                print("As you bring the paint can to your lips, you trip and fall. All the paint cans burst and the room get flooded with a multicolored flood. At least you lived a colorful life.\n")
                sys.exit("Ending Unlocked: Too much color")
            
            if user_input==room2_possibilites[1]:
                print("You suddenly realize the weight of the situation, and its too much. You cry, and the room gets filled with your salty water eye solution.")
                sys.exit("Ending Unlocked: Drowned")

            if user_input==room2_possibilites[2]:
                print("Suddenly, the cure for cancer hits you. Sadly, so does a bullet to the head.")
                sys.exit("Ending Unlocked: Assassinated by CIA")
            
            if user_input==room2_possibilites[3]:
                print("You take a step forward. Sadly, a banana peel has been waiting for you. You go from 1st to 12th place just like that.")
                sys.exit("Ending Unlocked: Mario Karted")

            if user_input==room2_possibilites[4]:
                print("As you walk back out the door, you trip over a paint can and hit your head...things suddenly go dark\n")
                room1()
    if user_input=="Quit":
        sys.exit("Quitted")


def room3():
    room3_possibilites=["Crank that soulja boy","Scream very loudly","Do a backflip","Hit the griddy", "Go back", "Quit"]

    print("You enter a room. Thats about it. It is a very empty room. \n")

    user_input=str(input("Crank that soulja boy, Scream very loudly, Do a backflip, Hit the griddy, Go back, or Quit?\n "))

    while user_input!=room3_possibilites[5]:
        while user_input not in room3_possibilites:
            print("Not valid input. Make sure to type your input exactly the same as they are in the prompt!\n")
            user_input=str(input("Enter left door, Enter front door, Search the room, Laugh, or Quit?\n "))

        while user_input in room3_possibilites:
            if user_input==room3_possibilites[0]:
                print("You start cranking that soulja boy, but you roll your ankle. The sudden pain puts you into cardiac arrest. You had a good run.\n")
                sys.exit("Ending Unlocked: Cranked that soulja boy too hard")
            if user_input==room3_possibilites[1]:
                print("You release an earth shaking screech. Sadly, the earth shook too much and the ceiling collapsed. What a rocky end.\n")
                sys.exit("Ending Unlocked: Crushed by rubble")
            if user_input==room3_possibilites[2]:
                print("You do a backflip, but forget you don't know how to do a back flip. This panics you, and you have a heart attack mid air\n")
                sys.exit("Ending Unlocked: Heart attack")
            if user_input==room3_possibilites[3]:
                print("You begin to hit the griddy, until you remember you never got that emote. This makes you extremely sad.")
                sys.exit("Ending Unlocked: Too Sad")
            if user_input==room3_possibilites[4]:
                print("As you start walking back to the original room, until you feel a small gust of wind. It floors you, banging your head in the process.")
                room1()
    if user_input=="Quit":
        sys.exit("Quitted")

room1()