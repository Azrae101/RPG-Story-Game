# Lobby #
import random

# To-do:
# lower() instead of different cases user_input

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
            elif location == 1 and 'book' not in inv:
                print("You are standing in front of a bookshelf.")
                print("All the books are lined up perfectly except for one book in particular.")
            elif location == 1 and 'book' in inv: 
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
            elif location == 4 and door == 0:
                print("You are standing in front of the secretary's door, this is locked.")
                print("There is a window")
            elif location == 4 and door == 1:
                print("You are standing in front of the secretary's door, it is open.")
                print("There is a window")
    
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
        elif 'leaflet' not in inv:
            print("You are not near any leaflet")
        else:
            print("You are already carrying a leaflet")

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

    if user_input == "drop leaflet" and 'leaflet' in inv:
            inv.remove("leaflet")
            print("Dropped.")
    elif user_input == "drop leaflet" and 'leaflet' not in inv: 
        print("You are not carrying a leaflet")

    ## Location == 1, North
    if user_input == "examine bookshelf" or user_input == "look at bookshelf" or user_input == "bookshelf":
        if location == 1:
            print("A particular book sticks out")
        else:
            print("You are not near any bookshelf")
    
    if user_input == "take book" or user_input == "pick up book":
        if location == 1 and 'book' not in inv:
            print("Taken.")
            inv.append("book")
        elif 'book' not in inv:
            print("You are not near any book")
        elif 'book' in inv:
            print("You are already carrying a book")
    
    if user_input == "pull the book out" and 'book' not in inv or user_input == "pull book out" and 'book' not in inv or user_input == "push bookshelf" or user_input == "kick bookshelf" or user_input == "hit bookshelf" or user_input == "punch bookshelf":
        print("You were crushed by the bookshelf")
        print("You died.")
        exit()
    elif user_input == "pull the book out" and 'book' in inv or user_input == "pull book out" and 'book' in inv:
        print("You are already carrying the book")

    # Book is in inventory and the screwdriver is not in inventory
    if user_input == "examine book" and 'book' in inv and 'screwdriver' not in inv or user_input == "look at book" and 'book' in inv and 'screwdriver' not in inv or user_input == "read book" and 'book' in inv and 'screwdriver' not in inv or user_input == "open book" and 'book' in inv and 'screwdriver' not in inv:
        print("The book is called:”Fahrenheit 451” and contains a screwdriver.")
    # Book is not in inventory
    if user_input == "examine book" and 'book' not in inv or user_input == "look at book" and 'book' not in inv or user_input == "read book" and 'book' not in inv or user_input == "open book" and 'book' not in inv:
        print("You are not carrying a book")
    # Book is in inventory and the screwdriver is in inventory
    if user_input == "examine book" and 'book' in inv and 'screwdriver' in inv or user_input == "open book" and 'book' in inv and 'screwdriver' in inv or user_input == "read book" and 'book' in inv and 'screwdriver' in inv or user_input == "open book"  and 'book' in inv and 'screwdriver' in inv:
        print("The book is called:”Fahrenheit 451” and is empty")
    
    # Screwdriver
    if user_input == "take screwdriver" or user_input == "pick up screwdriver":
        if location == 1 and 'screwdriver' not in inv and 'book' in inv:
            print("Taken.")
            inv.append("screwdriver")
        elif 'screwdriver' not in inv or 'book' not in inv:
            print("You are not near any screwdriver")
        elif 'screwdriver' in inv:
            print("You are already carrying a screwdriver")
    # Examine screwdriver
    if user_input == "look at screwdriver" and 'screwdriver' in inv or user_input == "screwdriver" and 'screwdriver' in inv or user_input == "view screwdriver" and 'screwdriver' in inv or user_input == "examine screwdriver" and 'screwdriver' in inv:
        print("It is a normal screwdriver")

    # Drop book
    if user_input == "drop book" and 'book' in inv:
            inv.remove("book")
            print("Dropped.")
    elif user_input == "drop book" and 'book' not in inv: 
        print("You are not carrying a book")

    # Drop screwdriver
    if user_input == "drop screwdriver" and 'screwdriver' in inv:
            inv.remove("screwdriver")
            print("Dropped.")
    elif user_input == "drop screwdriver" and 'screwdriver' not in inv: 
        print("You are not carrying a screwdriver")

    ## Location == 2, East 
    if location == 2:
        # Window
        if user_input == "Break window" or user_input == "Hit window" or user_input == "break window" or user_input == "Kick window" and window == 0:
            print("You broke the window")
            window += 1
        elif user_input == "Break window" or user_input == "Hit window" or user_input == "break window" and window == 1:
            print("The window is already broken")
        
        if user_input == "Examine window" or user_input == "examine window" and window == 0:
            print("Here is a window")
        elif user_input == "Examine window" or user_input == "examine window" and window == 1:
            print("This window is broken")
        
        if user_input == "Escape through window" or user_input == "go through window" and window == 0:
            print("This window is closed.")
        elif user_input == "Escape through window" or user_input == "go through window" and window == 1:
            print("You fell 2 stories")
            print("You died.")
            break # or exit()
        
        if user_input == "Look through window" or user_input == "look at window":
            print("You looked out the window, you had a heartattack from your fear of heights")
            print("You died.")
            break # or exit()

        # Fire extinguisher - cannot be picked up.
        if user_input == "take fire extinguisher" or user_input == "Take fire extinguisher" or user_input == "Take fe" or user_input == "take fe" and fire_extinguisher not in inv:
            print("Taken.")
            inv.append("fire extinguisher")
        elif user_input == "take fire extinguisher" or user_input == "Take fire extinguisher" or user_input == "Take fe" or user_input == "take fe" and fire_extinguisher in inv:
            print("You already took the fire extinguisher")

        if user_input == "Examine fire extinguisher" or user_input == "examine fire extinguisher" or user_input == "Examine fe" or user_input == "examine fe" and key not in inv:
           print("A key taped under the fire extinguisher is revealed")

        if user_input == "Use fire extinguisher" or user_input == "use fire extinguisher" or user_input == "Use fe" or user_input == "use fe" and fire_extinguisher in inv and heating_coils == True:
            print("The fire extinguisher only cools you down for a bit, but does not stop the oven from continuing to warm up.")
            health += 10
        elif user_input == "Use fire extinguisher" or user_input == "use fire extinguisher" and fire_extinguisher in inv and heating_coils == False:
            print("You were coated with white powder")
            health -= 10
        elif user_input == "Use fire extinguisher" or user_input == "use fire extinguisher" and fire_extinguisher not in inv:
            print("You do not have a fire extinguisher")

    # Drop fire extinguisher
    if user_input == "drop fire extinguisher" and 'fire extinguisher' in inv:
        inv.remove("fire extinguisher")
        print("Dropped.")
    elif user_input == "drop fire extinguisher" and 'fire extinguisher' not in inv:
        print("You do not have a fire extinguisher.")

    # Take key
    if user_input == "Take key" and location == 2 or user_input == "take key" and location == 2:
        print("Taken.")
        inv.append("key")
    elif user_input == "take key" and location != 2:
        print("There is no key here")
    elif user_input == "Examine fire extinguisher" or user_input == "examine fire extinguisher" and key in inv:
        print("There was a key here")

    # Drop key
    if user_input == "drop key" and 'key' in inv:
        inv.remove("key")
        print("Dropped.")
    elif user_input == "drop key" and 'key' not in inv:
        print("You do not have a key.")

    ## Location == 3, South
    # Door handle
    if location == 3:
        if user_input == "open door":
            if door_handle == False: 
                print("The handle breaks off and reveals an oven dial.")
                door_handle += 1
            elif door_handle == 1: 
                print("The oven dial beeps.")
        
        # Oven dial
        if user_input == "turn oven dial" or user_input == "turn dial":
            print("How many degrees?")
            ovendial += 1

        # Look at Oven dial
        if user_input == "look at oven dial" or user_input == "examine oven dial" or user_input == "oven dial" or user_input == "examine dial" or user_input == "oven":
            print("It is a oven dial that operates on fahrenheit degrees")

        # Heating coils    
        if user_input == "451" or user_input == "fahrenheit 451" and ovendial == 1:
            print("Turning the oven dial to 451 activated heating coils in the room, turning it into a giant oven, you are heating up, and have limited moves")
            heating_coils = True
        
        if user_input == "Hit the oven dial" or user_input == "Hit oven dial" or user_input == "Hit dial" or user_input == "hit the oven dial" or user_input == "hit oven dial" or user_input == "hit dial":
            print("The oven dial beeps")

    ## Location == 4, West
    if location == 4:
        if user_input == "break door":
            print("It does not budge")
        if user_input == "open door" and 'key' not in inv and door == 0:
            print("The door is locked")
        if user_input == "open door" and 'key' in inv or user_input == "use key" and 'key' in inv or user_input == "open key with door" and 'key' in inv or user_input == "use the key" and 'key' in inv:
            print("The door is unlocked")
            door = 1
        
        if user_input == "open window":
            print("Opening the window is not possible.")
        
        # Screwdriver options
        if user_input == "use screwdriver" and 'screwdriver' in inv:
            print("This does nothing")
        if user_input == "use screwdriver" and 'screwdriver' not in inv:
            print("You are not carrying a screwdriver")

    # Other commands
    if user_input == " ": # none
        print(random.choice(other_responses))
    if user_input == "diagnostic" or user_input == "health" or user_input == "hp" or user_input == "health power" or user_input == "status":
        if health == 100:
            print("Your health is perfect")
        else:
            print("Your health is: " + str(health) + "/100")
    if user_input == "jump": 
        print(random.choice(jump_responses))
        health -= 10
    if user_input == "hi" or user_input == "hello" or user_input == "hii" or user_input == "ello" or user_input == "howdy" or user_input == "hey" or user_input == "heyy":
        print(random.choice(hello))
    if user_input == "heyyy" or user_input == "heyyyy" or user_input == "heyyyyy" or user_input == "heyyyyyy":
        print("uhm, hi, are you okay?")
    if user_input == "bing chilling":
        print(random.choice(bingchill_responses))
    if user_input == "damn" or user_input == "shit" or user_input == "frick" or user_input == "fuck":
        print("Such language in a high-class establishment like this!")
    
    # kill
    if user_input == "kill":
        print("What do you want to kill?")
    if user_input == "kill mannequin":
        # mannequin requirements
        continue
    if user_input == "kill self" or user_input == "kill myself":
        print("What do you want to kill yourself with?")
    if user_input == "kill self with book" or user_input == "kill myself with book" or user_input == "kill self with leaflet" or user_input == "kill myself with leaflet":
        print("You cannot do that")

    # Health
    if health < 0:
        print("Your health was too low")
        print("You died.")
        print(" ")
        print("Hint: You can always check your health by typing 'health' or 'diagnostic'")
        exit()

#else:
#    print(random.choice(other_responses))

############################################################################################

### Secretary's office ###
