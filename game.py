# Lobby #
import random


# To-do:
# Can you stop the oven? or only escape through secretary's door?
# Rearrange so Secretary's office can be implemented

### Definitions:
room = 1
location = 0
health = 100
on_table = 0
moves = 0
warm = 0
sofa = 0
look_first = 0
destroyed_paintings = 0

# Objects
leaflet = False
leaflet_read = 0
book = False
fire_extinguisher = False
door_handle = False
heating_coils = False
secretary_door = False
ovendial = False
window = 0
key = 0
door = 0

# Lists
inv = []

hello = ["Hi","Heyy","Hey","Hii","Hello","Ello","Hiya","Howdy","Nice to meet you"]
bingchill_responses = ["冰淇淋","Bīngqílín","Ice-cream","Yummy","Guffe nam"]
jump_responses = ["WEEEEEOOOO","Are you proud of yourself?","Don't jump too high","Are you that excited about playing Kroz?"]
other_responses = ["Huh?","I beg your pardon?","What?","Come again?"]

# Start
print("KROZ: Escape the mystery mansion")
print("Copywrong (!) 2023, Escape room company, Inc. All rights reserved.")
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
    
    moves += 1

    # Know which room the user is in
    if user_input.lower() == "room" and room == 1:
        print("You are in the Lobby")
    if user_input.lower() == "room" and room == 2:
        print("You are in the Secretary's office")
    if user_input.lower() == "room" and room == 3:
        print("You are in the cabin")
    if user_input.lower() == "room" and room == 4:
        print("You are in the hospital")
    if user_input.lower() == "room" and room == 5:
        print("You are in the library")

    # Hints
    if room == 1 and door_handle == False and heating_coils == False and user_input.lower() == "h" or user_input.lower() == "hint":
        print("Try to examine the door to the south")
    elif user_input.lower() == "h" or user_input.lower() == "hint":
        print("If you don't know where to begin, you can try the following commands:")
        print("'look'")
        print("'middle','south', 'west', 'east' or 'north'")

    # Inventory
    if user_input.lower() == "i" or user_input.lower() == "inv" or user_input.lower() == "inventory":
        if len(inv) > 0: # If there is something in the list
            print("You are carrying:")
            for i in range (len(inv)):
                print(inv[i])
       
        if len(inv) == 0: # If the list is empty
            print("You are not carrying anything")

    # Quit
    if user_input.lower() == "q" or user_input.lower() == "quit" or user_input.lower() == "exit" or user_input.lower() == "quit game" or user_input.lower() == "exit game":
        exit()

############################################################################################
### Lobby ###
    if room == 1:
        # look
        if user_input.lower() == "look" or user_input.lower() == "look around" or user_input.lower() == "l" or user_input.lower() == "view room":
            if look_first == 0:
                look_first = 1
                print("You are in a sprawling, old and decrepit mansion that has a dark and foreboding atmosphere.")
                print("The mansion is surrounded by a large estate with overgrown gardens and a creepy forest, giving it a sense of isolation.")
                print("The interior of the mansion is just as eerie, with dimly lit halls, creaky floorboards, and musty furnishings.")
                print("The walls are adorned with old paintings and portraits, some of which seem to have faces that move or change expression.")
                print("There are secret passageways, locked doors, and hidden rooms to be discovered, each of which holds a piece of the mystery that needs to be unraveled.")
                print(" ")
            # Location: middle [0]
            if location == 0 or 'leaflet' not in inv:
                print("The Lobby")
                print("You are standing in a lobby, there is a leaflet on the coffee table.")
                print("There is a door in the south direction.")
            elif location == 0:
                print("The Lobby")
                print("You are standing in a lobby.")
                print("There is a door in the south direction.")
            # North
            elif location == 1 and 'book' not in inv:
                print("You are standing in front of a bookshelf.")
                print("All the books are lined up perfectly except for one book in particular.")
            elif location == 1 and 'book' in inv:
                print("You are standing in front of a bookshelf.")
                print("All the books are lined up perfectly.")
            # East
            if location == 2 and 'fire extinguisher' not in inv:
                print("You are standing in front of a window.")
                print("There is a fire extinguisher in front of the window.")
            elif location == 2 and 'fire extinguisher' in inv:
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
            elif location == 4 and door == 0:
                print("You are standing in front of the secretary's door, this is locked.")
                print("There is a window")
            elif location == 4 and door == 1:
                print("You are standing in front of the secretary's door, it is open.")
                print("There is a window")
    
        # Locations (Directions)
        if user_input.lower() == "m" or user_input.lower() == "middle" or user_input.lower() == "mid" or user_input.lower() == "go to coffee table" or user_input.lower() == "walk towards coffee table":
            location == 0
            if location == 0 and 'leaflet' not in inv:
                print("The Lobby")
                print("You are standing in a lobby, there is a leaflet on the coffee table beside the two sofas.")
                print("There is a door in the south direction.")
            if location == 0 and 'leaflet' in inv:
                print("The Lobby")
                print("You are standing in a lobby.")
                print("There is a coffee table in the middle of the Lobby by two sofas")
                print("There is a door in the south direction.")
        # North
        if user_input.lower() == "n" or user_input.lower() == "north" or user_input.lower() == "go north" or user_input.lower() == "go to bookshelf" or user_input.lower() == "walk towards bookshelf":
            location = 1
            if location == 1 and 'book' not in inv:
                print("You are standing in front of a bookshelf.")
                print("All the books are lined up perfectly except for one book in particular.")
            elif location == 1 and 'book' in inv:
                print("You are standing in front of a bookshelf.")
                print("All the books are lined up perfectly.")
        # East:
        if user_input.lower() == "e" or user_input.lower() == "east" or user_input.lower() == "go east" or user_input.lower() == "go to fire extinguisher" or user_input.lower() == "walk towards fire extinguisher":
            location = 2
            if location == 2 and 'fire extinguisher' not in inv:
                print("You are standing in front of a window.")
                print("There is a fire extinguisher in front of the window.")
            elif location == 2 and 'fire extinguisher' in inv:
                print("You are standing in front of a window.")
                print("The fire extinguisher was here.")
        # South:
        if user_input.lower() == "s" or user_input.lower() == "south" or user_input.lower() == "go south" or user_input.lower() == "go to door" or user_input.lower() == "walk towards door":
            location = 3
            if location == 3 and door_handle == False:
                print("You are standing in front of a door.")
            elif location == 3 and heating_coils == False:
                print("You are standing in front of a door, the oven dial flashes red.")
            elif location == 3:
                print("You are standing in front of a door.")
                print("The handle is missing, an oven dial appears instead.")
        # West:
        if user_input.lower() == "w" or user_input.lower() == "west" or user_input.lower() == "go west" or user_input.lower() == "go to secretary's door" or user_input.lower() == "walk towards secretary's door":
            location = 4
            if location == 4 and door == 0:
                print("You are standing in front of the secretary's door, this is locked.")
                print("There is a window")
            elif location == 4 and door == 1:
                print("You are standing in front of the secretary's door, it is open.")
                print("There is a window")
        # Other directions:
        if user_input.lower() == "go to window" or user_input.lower() == "walk to window" or user_input.lower() == "walk towards window" :
            print("There are multiple windows")

        ## Location == 0, Middle:
        
        # General commands in this location:
        if location == 0 and room == 1:
            if user_input.lower() == "look at table" or user_input.lower() == "look at the table" or user_input.lower() == "look at coffee table" or user_input.lower() == "look at the coffee table" or user_input.lower() == "examine table" or user_input.lower() == "examine the table" or user_input.lower() == "examine the coffee table" :
                print("There is a leaflet on the coffee table")
            if user_input.lower() == "go to table" or user_input.lower() == "go to the table" or user_input.lower() == "go to the coffee table" or user_input.lower() == "go to coffee table" or user_input.lower() == "look around coffee table"  or user_input.lower() == "look around table":
                print("You are standing beside the oval coffee table made out of mahogany wood")
                print("There is a leaflet on the coffee table")
            if user_input.lower() == "look under table" or user_input.lower() == "go under table":
                print("There is only dust under the table") 
                print("The dust makes you uncomfortable")
                health -= 10
            if user_input.lower() == "leave lobby" or user_input.lower() == "go out of lobby" or user_input.lower() == "escape the mansion" or user_input.lower() == "escape the lobby" or user_input.lower() == "escape" or user_input.lower() == "escape the mystery mansion" or user_input.lower() == "escape lobby":
                print("You cannot leave the lobby from here")
                print("There is an exit via the door in the south direction")
            if user_input.lower() == "what is kroz" or user_input.lower() == "kroz" or user_input.lower() == "zork":
                print("You will know, if you read the leaflet on the coffee table")
            if user_input.lower() == "i dont know" or user_input.lower() == "idk" or user_input.lower() == "i do not know" or user_input.lower() == "what to do" or user_input.lower() == "help" or user_input.lower() == "manual":
                print("If you don't know where to begin, you can try the following commands:")
                print("'look'")
                print("'take leaflet' and 'read leaflet'")
                print("'middle','south', 'west', 'east' or 'north'")
                print("If this doesn't help, you can always ask for a 'hint'")
            if user_input.lower() == "punch table" or user_input.lower() == "attack table" or user_input.lower() == "kick table" or user_input.lower() == "destroy table" or user_input.lower() == "eat leaflet":
                print("Why would you do that?")
                print("You hurt yourself")
                health -= 10
            if user_input.lower() == "destroy leaflet":
                print("You destroyed the leaflet by ripping it apart")
                leaflet = 2
            if user_input.lower() == "take table" or user_input.lower() == "grab table":
                print("You cannot do that.")
                print("The table is too heavy for you to carry.")
            if user_input.lower() == "are there any humans here" or user_input.lower() == "is there anyone here" or user_input.lower() == "anyone here":
                print("No, you are here by yourself. All alone.")
            if user_input.lower() == "go up on table" and on_table == 0 or user_input.lower() == "jump up on the table"  and on_table == 0 or user_input.lower() == "jump on table" and on_table == 0 or user_input.lower() == "go on table"  and on_table == 0 or user_input.lower() == "walk on table"  and on_table == 0:
                print("You feel like the king of the world...")
                print("...or at least this tiny lonesome lobby...")
                print("...It's actually a bit scary to be standing here...")
                print("...You feel the anxiety and fear kick in from being so high up...")
                print("You fainted, because you are scared of heights")
                exit()
            if user_input.lower() == "sit in sofas" and sofa == 0 or user_input.lower() == "go in sofas" and sofa == 0 or user_input.lower() == "sit in sofa" and sofa == 0 or user_input.lower() == "jump on sofa" and sofa == 0 or user_input.lower() == "jump on sofas" and sofa == 0:
                sofa = 1
                print("In this rather stressfull situation that you have put yourself in for money, you decide to relax for a bit in the sofas in the lobby")
                print("You remind yourself that you don't have unlimited time to escape this Mystery Mansion")
                print("Better get going")
                health += 10
            elif user_input.lower() == "sit in sofas" and sofa == 1 or user_input.lower() == "go in sofas" and sofa == 1 or user_input.lower() == "sit in sofa" and sofa == 1 or user_input.lower() == "jump on sofa" and sofa == 1 or user_input.lower() == "jump on sofas"and sofa == 1:
                print("You are a bit tired and just sitting in this sofa again made you fell asleep")
                print("You never woke up again for unknown reasons.")
                exit()
            elif user_input.lower() == "look at paintings" or user_input.lower() == "look at painting" or user_input.lower() == "look at portraits" or user_input.lower() == "look at portrait":
                print("It feels like the old paintings and portraits are looking at you, and are following your every step.")
                print("You better watch your back")
            elif user_input.lower() == "destroy paintings" or user_input.lower() == "destroy painting" or user_input.lower() == "destroy portraits" or user_input.lower() == "destroy portrait":
                if destroyed_paintings == 0:
                    destroyed_paintings = 1
                    print("You ruined the old and creepy paintings and portraits")
                    print("You have got a bad omen now")
                    print("The evil spirits hurt you")
                    health -= 10
                elif destroyed_paintings == 0:
                    print("You have already destroyed all of the paintings and portraits")
                    print("The evil spirits hurt you again")
                    health -= 10
            if user_input.lower() == "who am i" or user_input.lower() == "me":
                print("You are a retired pilot")

        # Leaflet
        if user_input.lower() == "take leaflet" or user_input.lower() == "grab the leaflet" or user_input.lower() == "grab leaflet" or user_input.lower() == "take the leaflet" or user_input.lower() == "pick up the leaflet" or user_input.lower() == "pick up leaflet":
            if location == 0 and 'leaflet' not in inv and leaflet != 2:
                print("Taken.")
                inv.append("leaflet")
            elif 'leaflet' not in inv and leaflet != 2:
                print("You are not near any leaflet")
            elif 'leaflet' not in inv and leaflet == 2:
                print("The leaflet is destroyed, so you cannot pick it up")
            else:
                print("You are already carrying a leaflet")

        if user_input.lower() == "inspect leaflet" or user_input.lower() == "examine leaflet":
            print("It is a normal leaflet")
            print("Maybe try reading it?")

        if user_input.lower() == "read leaflet" or user_input.lower() == "open leaflet" or user_input.lower() == "read the leaflet" or user_input.lower() == "open the leaflet" or user_input.lower() == "look in the leaflet" or user_input.lower() == "look at leaflet":
            leaflet_read = 1
            if 'leaflet' in inv:            
                print("page 1 out of 2")
                print("WELCOME TO KROZ!")
                print("KROZ is a game of adventure, danger, and low cunning.")
                print("In it you will explore some of the most amazing territory ever seen by mortals.")
                print("No computer should be without one!")
            else:
                print("You are not carrying a leaflet")


        if user_input.lower() == "turn to page 1" and leaflet_read == 1 or user_input.lower() == "read page 1"  and leaflet_read == 1 or user_input.lower() == "page 1"  and leaflet_read == 1 or user_input.lower() == "1" and leaflet_read == 1:
            if 'leaflet' in inv:            
                print("page 1 out of 2")
                print("WELCOME TO KROZ!")
                print("KROZ is a game of adventure, danger, and low cunning.")
                print("In it you will explore some of the most amazing territory ever seen by mortals.")
                print("No computer should be without one!")
            else:
                print("You are not carrying a leaflet")


        if user_input.lower() == "turn to page 2"  and leaflet_read == 1 or user_input.lower() == "read page 2"  and leaflet_read == 1 or user_input.lower() == "page 2"  and leaflet_read == 1 or user_input.lower() == "2"  and leaflet_read == 1:
            if 'leaflet' in inv:
                print("page 2 out of 2")
                print("You were promised a $10,000 prize, if able to escape an escape room called The Mystery Mansion.")
                print("Each puzzle room subjects the player to different dangers.")
                print("Some elements of the rooms reflect elements from the player's pasts, as the player survived a tragic event.")
                print("The only way to escape is to solve the puzzles.")
            else:
                print("You are not carrying a leaflet")


        if user_input.lower() == "drop leaflet" and 'leaflet' in inv:
                inv.remove("leaflet")
                print("Dropped.")
        elif user_input.lower() == "drop leaflet" and 'leaflet' not in inv:
            print("You are not carrying a leaflet")


        ## Location == 1, North
        
        # General commands
        if user_input.lower() == "align bookshelf" or user_input.lower() == "fix bookshelf" or user_input.lower() == "repair bookshelf" or user_input.lower() == "orient bookshelf" or user_input.lower() == "line books up":
            print("You try to orient the books and they are now lined up perfectly")
            print("One book messes up the bookshelf alignment once again")
            print("All the books are again lined up perfectly except for one book in particular.")
        # Book:
        if user_input.lower() == "examine bookshelf" or user_input.lower() == "look at bookshelf" or user_input.lower() == "bookshelf":
            if location == 1:
                print("A particular book sticks out")
            else:
                print("You are not near any bookshelf")
        if user_input.lower() == "look under bookshelf":
            print("A mouse attacks you from under the bookshelf")
            health -= 10
    
        if user_input.lower() == "take book" or user_input.lower() == "pick up book" or user_input.lower() == "grab the book":
            if location == 1 and 'book' not in inv:
                print("Taken.")
                inv.append("book")
            elif 'book' not in inv:
                print("You are not near any book")
            elif 'book' in inv:
                print("You are already carrying a book")
    
        if user_input.lower() == "pull the book out" and 'book' not in inv or user_input.lower() == "pull book out" and 'book' not in inv or user_input.lower() == "push bookshelf" or user_input.lower() == "kick bookshelf" or user_input.lower() == "hit bookshelf" or user_input.lower() == "punch bookshelf" or user_input.lower() == "climb bookshelf" or user_input.lower() == "climb the bookshelf" or user_input.lower() == "jump on the bookshelf" or user_input.lower() == "look behind the bookshelf" or user_input.lower() == "go in the bookshelf" or user_input.lower() == "touch the bookshelf":
            print("You were crushed by the bookshelf")
            print("You died.")
            exit()
        elif user_input.lower() == "pull the book out" and 'book' in inv or user_input.lower() == "pull book out" and 'book' in inv:
            print("You are already carrying the book")

        # Book is in inventory and the screwdriver is not in inventory
        if user_input.lower() == "examine book" and 'book' in inv and 'screwdriver' not in inv or user_input.lower() == "look at book" and 'book' in inv and 'screwdriver' not in inv or user_input.lower() == "read book" and 'book' in inv and 'screwdriver' not in inv or user_input.lower() == "open book" and 'book' in inv and 'screwdriver' not in inv:
            print("The book is called:”Fahrenheit 451” and contains a screwdriver.")
        # Book is not in inventory
        if user_input.lower() == "examine book" and 'book' not in inv or user_input.lower() == "look at book" and 'book' not in inv or user_input.lower() == "read book" and 'book' not in inv or user_input.lower() == "open book" and 'book' not in inv:
            print("You are not carrying a book")
        # Book is in inventory and the screwdriver is in inventory
        if user_input.lower() == "examine book" and 'book' in inv and 'screwdriver' in inv or user_input.lower() == "open book" and 'book' in inv and 'screwdriver' in inv or user_input.lower() == "read book" and 'book' in inv and 'screwdriver' in inv or user_input.lower() == "open book"  and 'book' in inv and 'screwdriver' in inv:
            print("The book is called:”Fahrenheit 451” and is empty")
    
        # Screwdriver
        if user_input.lower() == "take screwdriver" or user_input.lower() == "pick up screwdriver":
            if location == 1 and 'screwdriver' not in inv and 'book' in inv or 'book' in inv and 'screwdriver' not in inv:
                print("Taken.")
                inv.append("screwdriver")
            elif 'screwdriver' not in inv or 'book' not in inv:
                print("You are not near any screwdriver")
            elif 'screwdriver' in inv:
                print("You are already carrying a screwdriver")
        # Examine screwdriver
        if user_input.lower() == "look at screwdriver" and 'screwdriver' in inv or user_input.lower() == "screwdriver" and 'screwdriver' in inv or user_input.lower() == "view screwdriver" and 'screwdriver' in inv or user_input.lower() == "examine screwdriver" and 'screwdriver' in inv:
            print("It is a normal screwdriver")

        # Drop book
        if user_input.lower() == "drop book" and 'book' in inv:
                inv.remove("book")
                print("Dropped.")
        elif user_input.lower() == "drop book" and 'book' not in inv:
            print("You are not carrying a book")

        # Drop screwdriver
        if user_input.lower() == "drop screwdriver" and 'screwdriver' in inv:
                inv.remove("screwdriver")
                print("Dropped.")
        elif user_input.lower() == "drop screwdriver" and 'screwdriver' not in inv:
            print("You are not carrying a screwdriver")


        ## Location == 2, East
        if location == 2:
            # Window
            if user_input.lower() == "open window" and 'screwdriver' not in inv:
                print("Opening the window is not possible")
            
            if user_input.lower() == "break window" and window == 0 or user_input.lower() == "hit window" and window == 0 or user_input.lower() == "kick window" and window == 0 or user_input.lower() == "break window" and window == 0 or user_input.lower() == "open window" and window == 0 and 'screwdriver' in inv or user_input.lower() == "open window with screwdriver" and window == 0 and 'screwdriver' in inv or user_input.lower() == "use screwdriver on window" and window == 0 and 'screwdriver' in inv:
                print("You broke the window")
                window = 1
            elif user_input.lower() == "break window" or user_input.lower() == "hit window":
                print("The window is already broken")
        
            if user_input.lower() == "examine window" and window == 0 or user_input.lower() == "inspect window" and window == 0:
                print("Here is a window")
            elif user_input.lower() == "examine window" and window == 1:
                print("This window is broken")
        
            if user_input.lower() == "Escape through window" or user_input.lower() == "go through window" and window == 0:
                print("This window is closed.")
            elif user_input.lower() == "Escape through window" or user_input.lower() == "go through window" and window == 1:
                print("You fell 2 stories")
                print("You died.")
                break # or exit()
        
            if user_input.lower() == "Look through window" or user_input.lower() == "look at window" or user_input.lower() == "look out window" or user_input.lower() == "look out of window" or user_input.lower() == "look out of the window":
                print("You looked out the window, you had a heartattack from your fear of heights")
                print("You died.")
                break # or exit()


            # Fire extinguisher - cannot be picked up.
            if user_input.lower() == "take fire extinguisher" or user_input.lower() == "Take fire extinguisher" or user_input.lower() == "Take fe" or user_input.lower() == "take fe" and fire_extinguisher not in inv:
                print("Taken.")
                inv.append("fire extinguisher")
            elif user_input.lower() == "take fire extinguisher" or user_input.lower() == "Take fire extinguisher" or user_input.lower() == "Take fe" or user_input.lower() == "take fe" and fire_extinguisher in inv:
                print("You already took the fire extinguisher")


            if user_input.lower() == "examine fire extinguisher" and key not in inv or user_input.lower() == "examine fe" and key not in inv or user_input.lower() == "look at fe" and key not in inv or user_input.lower() == "look at fire extinguisher" and key not in inv:
                print("A key taped under the fire extinguisher is revealed")


        if user_input.lower() == "use fire extinguisher" or user_input.lower() == "use fe" and 'fire extinguisher' in inv and warm == 1:
            print("The fire extinguisher only cools you down for a bit, but does not stop the oven from continuing to warm up.")
            health += 10
        elif user_input.lower() == "use fire extinguisher" and 'fire extinguisher' in inv and warm == 0 or user_input.lower() == "use fe" and 'fire extinguisher' in inv and warm == 0:
            print("You were coated with white powder")
            health -= 10
        elif user_input.lower() == "use fire extinguisher" and 'fire extinguisher' not in inv:
            print("You do not have a fire extinguisher")


        # Drop fire extinguisher
        if user_input.lower() == "drop fire extinguisher" and 'fire extinguisher' in inv:
            inv.remove("fire extinguisher")
            print("Dropped.")
        elif user_input.lower() == "drop fire extinguisher" and 'fire extinguisher' not in inv:
            print("You do not have a fire extinguisher.")


        # Take key
        if user_input.lower() == "take key" and location == 2:
            print("Taken.")
            inv.append("key")
        elif user_input.lower() == "take key" and location != 2:
            print("There is no key here")
        elif user_input.lower() == "examine fire extinguisher" and key in inv:
            print("There was a key here")
        # Drop key
        if user_input.lower() == "drop key" and 'key' in inv:
            inv.remove("key")
            print("Dropped.")
        elif user_input.lower() == "drop key" and 'key' not in inv:
            print("You do not have a key.")


        ## Location == 3, South
        # Door handle
        if location == 3:
            if user_input.lower() == "open door" or user_input.lower() == "enter door":
                if door_handle == False:
                    print("The handle breaks off and reveals an oven dial.")
                    door_handle += 1
                elif door_handle == 1:
                    print("The oven dial beeps.")
        
            if user_input.lower() == "punch door" or user_input.lower() == "attack door" or user_input.lower() == "kick door" or user_input.lower() == "destroy door" or user_input.lower() == "run into door":
                print("Nothing happens")
                print("You hurt yourself")
                health -= 10

            # Oven dial
            if user_input.lower() == "turn oven dial" or user_input.lower() == "turn dial" or user_input.lower() == "use oven dial" or user_input.lower() == "use dial" or user_input.lower() == "use oven ":
                print("How many degrees?")
                ovendial = 1

            # Look at Oven dial
            if user_input.lower() == "look at oven dial" or user_input.lower() == "examine oven dial" or user_input.lower() == "oven dial" or user_input.lower() == "examine dial" or user_input.lower() == "oven" or user_input.lower() == "inspect oven dial" or user_input.lower() == "check dial" or user_input.lower() == "check oven" or user_input.lower() == "check oven dial":
                print("It is a oven dial that operates on Fahrenheit degrees")

            # Heating coils    
            if user_input.lower() == "451" or user_input.lower() == "fahrenheit 451" and ovendial == 1:
                print("Turning the oven dial to 451 activated heating coils in the room, turning it into a giant oven, you are heating up, and have limited moves")
                heating_coils = True
                moves = 0
                warm = 1
        if warm == 1 and moves > 5 and secretary_door == 0:
            print("You have used all your moves")
            print("The room has become too hot")
            print("You died from overheating.")
            exit()
        if warm == 1 and secretary_door == 0:
            print("The room is getting warmer")
            health -= 10
        if warm == 1 and secretary_door == 1:
            print("You succesfully escaped the lobby")

            if user_input.lower() == "fix dial" or user_input.lower() == "repair dial" or user_input.lower() == "fix oven" or user_input.lower() == "repair oven":
                print("You cannot repair the dial")

            if user_input.lower() == "hit the oven dial" or user_input.lower() == "hit oven dial" or user_input.lower() == "hit dial":
                print("The oven dial beeps")

        # Take handle
        if user_input.lower() == "fix handle" or user_input.lower() == "repair handle":
            print("You cannot repair the handle")
        if user_input.lower() == "take handle" and location == 3 and 'handle' not in inv or user_input.lower() == "grab handle" and location == 3 and 'handle' not in inv or user_input.lower() == "pick up handle" and location == 3 and 'handle' not in inv:
            print("Taken.")
            inv.append("handle")
        elif user_input.lower() == "take handle" and 'handle' in inv:
            print("You are already carrying a handle")
        elif user_input.lower() == "take handle" and location != 3:
            print("There is no handle here")
        # Drop handle
        if user_input.lower() == "drop handle" and 'handle' in inv:
            inv.remove("handle")
            print("Dropped.")
        elif user_input.lower() == "drop handle" and 'handle' not in inv:
            print("You do not have a handle.")


        ## Location == 4, West
        if location == 4:
            if user_input.lower() == "break door":
                print("It does not budge")
            if user_input.lower() == "open door" and 'key' not in inv and door == 0 or user_input.lower() == "look at door" and 'key' not in inv and door == 0 or user_input.lower() == "examine door" and 'key' not in inv and door == 0 or user_input.lower() == "view door" and 'key' not in inv and door == 0 or user_input.lower() == "inspect door" and 'key' not in inv and door == 0 or user_input.lower() == "examine door" and 'key' not in inv and door == 0 or user_input.lower() == "enter door" and 'key' not in inv and door == 0:
                print("The door is locked")
            if user_input.lower() == "open door" and door == 1 or user_input.lower() == "look at door" and door == 1 or user_input.lower() == "examine door" and door == 1 or user_input.lower() == "view door" and door == 1 or user_input.lower() == "inspect door" and door == 1 or user_input.lower() == "examine door" and door == 1:
                print("The door is open")
            if user_input.lower() == "open door" and 'key' in inv and door == 0 or user_input.lower() == "use key" and 'key' in inv and door == 0 or user_input.lower() == "open key with door" and 'key' in inv and door == 0 or user_input.lower() == "use the key" and 'key' in inv and door == 0 or user_input.lower() == "look at door" and 'key' in inv and door == 0 or user_input.lower() == "examine door" and 'key' in inv and door == 0 or user_input.lower() == "view door" and 'key' in inv and door == 0 or user_input.lower() == "inspect door" and 'key' in inv and door == 0 or user_input.lower() == "examine door" and 'key' in inv and door == 0:
                print("The door is unlocked")
                door = 1
                secretary_door = 1
            if user_input.lower() == "enter door" and secretary_door == 1 or user_input.lower() == "enter door" and 'key' in inv and door == 0:
                room = 2
                if warm == 0:
                        print("You succesfully escaped the lobby")
            if warm == 1 and room == 2:
                warm = 0

            if user_input.lower() == "find key" and 'key' not in inv:
                print("You must look elsewhere")

            if user_input.lower() == "open window" or user_input.lower() == "escape through window" or user_input.lower() == "jump through window" or user_input.lower() == "jump out of the window":
                print("Opening the window is not possible.")

            if user_input.lower() == "look out of window" or user_input.lower() == "look at window" or user_input.lower() == "go to window" or user_input.lower() == "examine window" or user_input.lower() == "look at window" or user_input.lower() == "go to window" or user_input.lower() == "examine window"  or user_input.lower() == "view window" or user_input.lower() == "inspect window":
                print("You looked out the window, you had a heartattack from your fear of heights")
                print("You died.")
                break # or exit()
            if user_input.lower() == "break window" or user_input.lower() == "hit window" or user_input.lower() == "kick window" or user_input.lower() == "punch window":
                print("You cannot break this window")
        
            # Screwdriver options
        if user_input.lower() == "use screwdriver" and 'screwdriver' in inv:
            print("This does nothing")
        if user_input.lower() == "use screwdriver" and 'screwdriver' not in inv:
            print("You are not carrying a screwdriver")

############################################################################################
### Secretary's office ###
    if room == 2:
        if user_input == "hej":
            continue
        if user_input.lower() == "look in mirror" or user_input.lower() == "look at self in mirror":
            print("You look yourself in the eyes for the first time in a while")
            print("You remember what you did...")
            print("You remember all those people, whose lives you ruined")
            print("The guilt makes your stomach turn and twist")
            print("You got hurt by the trauma and guilt")
            health -= 10
        if user_input.lower() == "something, learn about yourself":
            print("You are a retired pilot, who caused a tragic plane accident, killing all passengers in the plane, except yourself.")
            print("Since the accident, you have been retired, scared of heights and flight and in insane insurance dept.")
            print("You were promised a $10,000 prize, if able to escape an escape room called The Mystery Mansion.")

############################################################################################
### The Cabin ###
    if room == 3:
        if user_input == "hej":
            continue
############################################################################################
### The Hospital ###
    if room == 4:
        if user_input == "hej":
            continue
############################################################################################
### The Library ###
    if room == 2:
        if user_input == "hej":
            continue

############################################################################################
    # Other commands
    if user_input.lower() == " ": # none
        print(random.choice(other_responses))
    if user_input.lower() == "diagnostic" or user_input.lower() == "health" or user_input.lower() == "hp" or user_input.lower() == "health power" or user_input.lower() == "status":
        if health == 100:
            print("Your health is perfect")
        else:
            print("Your health is: " + str(health) + "/100")
    if user_input.lower() == "jump":
        print(random.choice(jump_responses))
        health -= 10
    if user_input.lower() == "hi" or user_input.lower() == "hello" or user_input.lower() == "hii" or user_input.lower() == "ello" or user_input.lower() == "howdy" or user_input.lower() == "hey" or user_input.lower() == "heyy":
        print(random.choice(hello))
    if user_input.lower() == "heyyy" or user_input.lower() == "heyyyy" or user_input.lower() == "heyyyyy" or user_input.lower() == "heyyyyyy":
        print("uhm, hi, are you okay?")
    if user_input.lower() == "bing chilling":
        print(random.choice(bingchill_responses))
    if user_input.lower() == "damn" or user_input.lower() == "shit" or user_input.lower() == "frick" or user_input.lower() == "fuck":
        print("Such language in a high-class establishment like this!")
    if user_input.lower() == "nice" or user_input.lower() == "great" or user_input.lower() == "amazing" or user_input.lower() == "awesome":
        print("I'm glad you like it")
    if user_input.lower() == "go back" or user_input.lower() == "back" or user_input.lower() == "take back" or user_input.lower() == "undo":
        print("There is no turning back :)")  
    if user_input.lower() == "open window" and location !=2 and location !=4:
        print("There is no window here")
    if user_input.lower() == "open door" and location !=3 and location !=4 or user_input.lower() == "enter door" and location !=3 and location !=4:
        print("There is no door here")
    if user_input.lower() == "walk forward" or user_input.lower() == "go forward" or user_input.lower() == "forward" or user_input.lower() == "up" or user_input.lower() == "down" or user_input.lower() == "northeast" or user_input.lower() == "ne" or user_input.lower() == "northwest" or user_input.lower() == "nw" or user_input.lower() == "southeast" or user_input.lower() == "se" or user_input.lower() == "southwest" or user_input.lower() == "sw" or user_input.lower() == "walk backwards" or user_input.lower() == "backwards" or user_input.lower() == "go backwards":
        print("You cannot go that direction, but you can try the following commands:")
        print("'middle','south', 'west', 'east' or 'north'")
        print("If this doesn't help, you can always ask for a 'hint'")
   
    # kill
    if user_input.lower() == "kill":
        print("What do you want to kill?")
    if user_input.lower() == "kill mannequin":
        # mannequin requirements
        continue
    if user_input.lower() == "kill self" or user_input.lower() == "kill myself":
        print("What do you want to kill yourself with?")
    if user_input.lower() == "kill self with book" or user_input.lower() == "kill myself with book" or user_input.lower() == "kill self with leaflet" or user_input.lower() == "kill myself with leaflet":
        print("You cannot do that")
    
    if user_input.lower() == "punch self" or user_input.lower() == "hurt self" or user_input.lower() == "kick self":
        print("Why would you do that?")
        print("You hurt yourself.")
        health -= 10

    # Health
    if health < 0:
        print("Your health was too low")
        print("You died.")
        print(" ")
        print("Hint: You can always check your health by typing 'health' or 'diagnostic'")
        exit()

    # Typing wrong codes and numbers
    if user_input.isnumeric():
        if user_input == "451" and room == 1 and location == 3:
            continue
        elif user_input.isnumeric():
            print("Typing that number does nothing")
