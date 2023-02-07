# Lobby #
import random

### Definitions:
room = 1
location = 0
health = 100

# Objects
leaflet = False
leaflet_read = 0

book = False
fire_extinguisher = False
door_handle = False
heating_coils = False
secretary_door = False

# Lists
inv = []

hello = ["Hi","Heyy","Hey","Hii","Hello","Ello","Hiya","Howdy","Nice to meet you"]
bingchill_responses = ["冰淇淋","Bīngqílín","Ice-cream","Yummy","Guffe nam"]
jump_responses = ["WEEEEEOOOO","Are you proud of yourself?","Don't jump too high","Are you that excited about playing Kroz?"]
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
            for i in range (len(inv)):
                print(inv[i])
        
        if len(inv) == 0: # If the list is empty
            print("You are not carrying anything")

    # look
    if user_input == "look" or user_input == "Look" or user_input == "l":
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
    
    # Locations (Directions)
    if user_input == "m" or user_input == "middle" or user_input == "mid":
        location = 0
        print("The Lobby")
        print("You are standing in a lobby.")
        print("There is a door in the south direction.")
    # North
    if user_input == "n" or user_input == "north":
        location = 1
        print("You are standing in front of a bookshelf.")
    # East:
    if user_input == "e" or user_input == "east":
        location = 2
        print("You are standing in front of a window.")
    # South:
    if user_input == "s" or user_input == "south":
        location = 3
        print("You are standing in front of a door.")
    # West:
    if user_input == "w" or user_input == "west":
        location = 4
        print("You are standing in front of the secretary's door.")

    # Quit
    if user_input == "q" or user_input == "quit" or user_input == "exit" or user_input == "quit game" or user_input == "exit game":
        exit()

    ### Objects:

    ## Location == 0, Middle: 
    # Leaflet 
    if user_input == "take leaflet":
        if location == 0 and 'leaflet' not in inv:
            print("Taken.")
            inv.append("leaflet")

    if user_input == "read leaflet":
        leaflet_read = 1
        if 'leaflet' in inv:            
            print("page 1 out of 2")
            print("WELCOME TO KROZ!")
            print("KROZ is a game of adventure, danger, and low cunning.")
            print("In it you will explore some of the most amazing territory ever seen by mortals.")
            print("No computer should be without one!")
        else:
            print("You are not carrying a leaflet")

    if user_input == "turn to page 1" and leaflet_read == 1 or user_input == "read page 1"  and leaflet_read == 1 or user_input == "page 1"  and leaflet_read == 1 or user_input == "1" and leaflet_read == 1:
        if 'leaflet' in inv:            
            print("page 1 out of 2")
            print("WELCOME TO KROZ!")
            print("KROZ is a game of adventure, danger, and low cunning.")
            print("In it you will explore some of the most amazing territory ever seen by mortals.")
            print("No computer should be without one!")
        else:
            print("You are not carrying a leaflet")

    if user_input == "turn to page 2"  and leaflet_read == 1 or user_input == "read page 2"  and leaflet_read == 1 or user_input == "page 2"  and leaflet_read == 1 or user_input == "2"  and leaflet_read == 1:
        if 'leaflet' in inv:
            print("page 2 out of 2")
            print("You were promised a $10,000 prize, if able to escape an escape room called The Mystery Mansion.")
            print("Each puzzle room subjects the player to different dangers.")
            print("Some elements of the rooms reflect elements from the player's pasts, as the player survived a tragic event.")
            print("The only way to escape is to solve the puzzles.")
        else:
            print("You are not carrying a leaflet")

    if user_input == "drop leaflet":
        if 'leaflet' in inv:
            inv.remove("leaflet")
            print("Dropped.")

    ## Location == 1, North

    ## Location == 2, East 

    ## Location == 3, South

    ## Location == 4, West

    # Other commands
    if user_input == " ": # none
        print(random.choice(other_responses))
    if user_input == "diagnostic" or user_input == "health" or user_input == "hp" or user_input == "health power" or user_input == "status":
        if health == 100:
            print("Your health is perfect")
        else:
            print("Your health is: " + health + "/100")
    if user_input == "jump": 
        print(random.choice(jump_responses))
    if user_input == "hi" or user_input == "hello" or user_input == "hii" or user_input == "ello" or user_input == "howdy" or user_input == "hey" or user_input == "heyy":
        print(random.choice(hello))
    if user_input == "heyyy" or user_input == "heyyyy" or user_input == "heyyyyy" or user_input == "heyyyyyy":
        print("uhm, hi, are you okay?")
    if user_input == "bing chilling":
        print(random.choice(bingchill_responses))
    if user_input == "damn" or user_input == "shit" or user_input == "frick" or user_input == "fuck":
        print("Such language in a high-class establishment like this!")
    #else:
    #    print(random.choice(other_responses))

