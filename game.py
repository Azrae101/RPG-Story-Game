# Lobby #
import random

### Definitions:
room = 1
location = 0

# Objects
leaflet = False
book = False
fire_extinguisher = False
door_handle = False
heating_coils = False
secretary_door = False

# Lists
inv = []
other_responses = ["Huh?","I beg your pardon?","What?","Come again?"]

# Start
print("KROZ: Escape the mystery mansion")
print("Copyright (c) 2023, Escape room company, Inc. All rights reserved.")
print("KROZ is a registered trademark of Escape room company, Inc.")
print("Revision 1 / Serial number 000001")
print(" ")
print("You are standing in a lobby, there is a leaflet on the coffee table.")
print("There is a door in the south direction.")
print(" ")
print("What are you going to do?")

# Inputs
while True: # while is running:
    
    user_input = input(" ")

    # Hints
    if room == 1 and door_handle == False and heating_coils == False and user_input == "h" or user_input == "H" or user_input == "hint":
        print("Try to examine the door to the south")


    # Inventory 
    if user_input == "i" or user_input == "inv" or user_input == "inventory":
        if len(inv) > 0: # If there is something in the list
            print("You are carrying:")
            print(inv)
        
        if len(inv) == 0: # If the list is empty
            print("You are not carrying anything")
        if inv:
            print("You are carrying:")
            print(inv)

    # look
    if user_input == "look":
        if room == 1: # lobby
            # Location: middle [0]
            if location == 0 and leaflet == False or leaflet in inv:
                print("The Lobby")
                print("You are standing in a lobby, there is a leaflet on the coffee table.")
                print("There is a door in the south direction.")
            elif location == 0:
                print("The Lobby")
                print("You are standing in a lobby.")
                print("There is a door in the south direction.")

            # North
            elif location == 1 and book == False or book in inv:
                print("You are standing in front of a bookshelf.")
                print("All the books are lined up perfectly except for one book in particular.")
            elif location == 1: 
                print("You are standing in front of a bookshelf.")
                print("All the books are lined up perfectly.")

            # East
            elif location == 2 and fire_extinguisher == False or fire_extinguisher in inv:
                print("You are standing in front of a fire extinguisher.")
            elif location == 2:
                print("You are standing in front of a window.")
                print("The fire extinguisher was here.")

            # South
            elif location == 3 and door_handle == False:
                print("You are standing in front of a door.")
            elif location == 3 and heating_coils == False:
                print("You are standing in front of a door, the oven dial flashes red.")
            elif location == 3:
                print("You are standing in front of a door.")
                print("The handle is missing, an oven dial appears instead.")

            # West
            elif location == 4 and secretary_door == False:
                print("You are standing in front of the secretary's door, this is locked.")
            elif location == 4:
                print("You are standing in front of the secretary's door, it is open.")

    elif 
    
    
    # Inventory # PROBLEM HERE: keeps on printing even though user_input is not correct
    elif user_input == "i" or "inv" or "inventory":
        if not inv: 
            print("You are not carrying anything")
        elif inv:
            print("You are carrying:")
            print(inv)
    
    # Quit
    elif user_input == "q" or user_input == "quit" or user_input ==  "exit" or user_input ==  "quit game" or user_input ==  "exit game":
        exit()
    
    # Other responses
    elif user_input == "":
        print(random.choice(other_responses))