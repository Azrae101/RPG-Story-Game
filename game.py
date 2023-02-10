# Lobby #
import random


# To-do:
# user_input.lower() instead of different cases user_input.lower()
# Rearrange so Secretary's office can be implemented, whilst ob


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
    if room == 1 and door_handle == False and heating_coils == False and user_input.lower().lower() == "h" or user_input.lower() == "hint":
        print("Try to examine the door to the south")


    # Inventory
    if user_input.lower() == "i" or user_input.lower() == "inv" or user_input.lower() == "inventory":
        if len(inv) > 0: # If there is something in the list
            print("You are carrying:")
            for i in range (len(inv)):
                print(inv[i])
       
        if len(inv) == 0: # If the list is empty
            print("You are not carrying anything")


    # look
    if user_input.lower() == "look" or user_input.lower() == "Look" or user_input.lower() == "l":
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
    if user_input.lower() == "m" or user_input.lower() == "middle" or user_input.lower() == "mid":
        location = 0
        print("The Lobby")
        print("You are standing in a lobby.")
        print("There is a door in the south direction.")
    # North
    if user_input.lower() == "n" or user_input.lower() == "north":
        location = 1
        print("You are standing in front of a bookshelf.")
    # East:
    if user_input.lower() == "e" or user_input.lower() == "east":
        location = 2
        print("You are standing in front of a window.")
    # South:
    if user_input.lower() == "s" or user_input.lower() == "south":
        location = 3
        print("You are standing in front of a door.")
    # West:
    if user_input.lower() == "w" or user_input.lower() == "west":
        location = 4
        print("You are standing in front of the secretary's door.")


    # Quit
    if user_input.lower() == "q" or user_input.lower() == "quit" or user_input.lower() == "exit" or user_input.lower() == "quit game" or user_input.lower() == "exit game":
        exit()


    ### Objects:


    ## Location == 0, Middle:
    # Leaflet
    if user_input.lower() == "take leaflet":
        if location == 0 and 'leaflet' not in inv:
            print("Taken.")
            inv.append("leaflet")
        elif 'leaflet' not in inv:
            print("You are not near any leaflet")
        else:
            print("You are already carrying a leaflet")


    if user_input.lower() == "read leaflet":
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
    if user_input.lower() == "examine bookshelf" or user_input.lower() == "look at bookshelf" or user_input.lower() == "bookshelf":
        if location == 1:
            print("A particular book sticks out")
        else:
            print("You are not near any bookshelf")
   
    if user_input.lower() == "take book" or user_input.lower() == "pick up book":
        if location == 1 and 'book' not in inv:
            print("Taken.")
            inv.append("book")
        elif 'book' not in inv:
            print("You are not near any book")
        elif 'book' in inv:
            print("You are already carrying a book")
   
    if user_input.lower() == "pull the book out" and 'book' not in inv or user_input.lower() == "pull book out" and 'book' not in inv or user_input.lower() == "push bookshelf" or user_input.lower() == "kick bookshelf" or user_input.lower() == "hit bookshelf" or user_input.lower() == "punch bookshelf":
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
        if location == 1 and 'screwdriver' not in inv and 'book' in inv:
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
        if user_input.lower() == "Break window" or user_input.lower() == "Hit window" or user_input.lower() == "break window" or user_input.lower() == "Kick window" and window == 0:
            print("You broke the window")
            window += 1
        elif user_input.lower() == "Break window" or user_input.lower() == "Hit window" or user_input.lower() == "break window" and window == 1:
            print("The window is already broken")
       
        if user_input.lower() == "Examine window" or user_input.lower() == "examine window" and window == 0:
            print("Here is a window")
        elif user_input.lower() == "Examine window" or user_input.lower() == "examine window" and window == 1:
            print("This window is broken")
       
        if user_input.lower() == "Escape through window" or user_input.lower() == "go through window" and window == 0:
            print("This window is closed.")
        elif user_input.lower() == "Escape through window" or user_input.lower() == "go through window" and window == 1:
            print("You fell 2 stories")
            print("You died.")
            break # or exit()
       
        if user_input.lower() == "Look through window" or user_input.lower() == "look at window":
            print("You looked out the window, you had a heartattack from your fear of heights")
            print("You died.")
            break # or exit()


        # Fire extinguisher - cannot be picked up.
        if user_input.lower() == "take fire extinguisher" or user_input.lower() == "Take fire extinguisher" or user_input.lower() == "Take fe" or user_input.lower() == "take fe" and fire_extinguisher not in inv:
            print("Taken.")
            inv.append("fire extinguisher")
        elif user_input.lower() == "take fire extinguisher" or user_input.lower() == "Take fire extinguisher" or user_input.lower() == "Take fe" or user_input.lower() == "take fe" and fire_extinguisher in inv:
            print("You already took the fire extinguisher")


        if user_input.lower() == "Examine fire extinguisher" or user_input.lower() == "examine fire extinguisher" or user_input.lower() == "Examine fe" or user_input.lower() == "examine fe" and key not in inv:
           print("A key taped under the fire extinguisher is revealed")


        if user_input.lower() == "Use fire extinguisher" or user_input.lower() == "use fire extinguisher" or user_input.lower() == "Use fe" or user_input.lower() == "use fe" and fire_extinguisher in inv and heating_coils == True:
            print("The fire extinguisher only cools you down for a bit, but does not stop the oven from continuing to warm up.")
            health += 10
        elif user_input.lower() == "Use fire extinguisher" or user_input.lower() == "use fire extinguisher" and fire_extinguisher in inv and heating_coils == False:
            print("You were coated with white powder")
            health -= 10
        elif user_input.lower() == "Use fire extinguisher" or user_input.lower() == "use fire extinguisher" and fire_extinguisher not in inv:
            print("You do not have a fire extinguisher")


    # Drop fire extinguisher
    if user_input.lower() == "drop fire extinguisher" and 'fire extinguisher' in inv:
        inv.remove("fire extinguisher")
        print("Dropped.")
    elif user_input.lower() == "drop fire extinguisher" and 'fire extinguisher' not in inv:
        print("You do not have a fire extinguisher.")


    # Take key
    if user_input.lower() == "Take key" and location == 2 or user_input.lower() == "take key" and location == 2:
        print("Taken.")
        inv.append("key")
    elif user_input.lower() == "take key" and location != 2:
        print("There is no key here")
    elif user_input.lower() == "Examine fire extinguisher" or user_input.lower() == "examine fire extinguisher" and key in inv:
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
        if user_input.lower() == "open door":
            if door_handle == False:
                print("The handle breaks off and reveals an oven dial.")
                door_handle += 1
            elif door_handle == 1:
                print("The oven dial beeps.")
       
        # Oven dial
        if user_input.lower() == "turn oven dial" or user_input.lower() == "turn dial":
            print("How many degrees?")
            ovendial += 1


        # Look at Oven dial
        if user_input.lower() == "look at oven dial" or user_input.lower() == "examine oven dial" or user_input.lower() == "oven dial" or user_input.lower() == "examine dial" or user_input.lower() == "oven":
            print("It is a oven dial that operates on fahrenheit degrees")


        # Heating coils    
        if user_input.lower() == "451" or user_input.lower() == "fahrenheit 451" and ovendial == 1:
            print("Turning the oven dial to 451 activated heating coils in the room, turning it into a giant oven, you are heating up, and have limited moves")
            heating_coils = True
       
        if user_input.lower() == "Hit the oven dial" or user_input.lower() == "Hit oven dial" or user_input.lower() == "Hit dial" or user_input.lower() == "hit the oven dial" or user_input.lower() == "hit oven dial" or user_input.lower() == "hit dial":
            print("The oven dial beeps")


    ## Location == 4, West
    if location == 4:
        if user_input.lower() == "break door":
            print("It does not budge")
        if user_input.lower() == "open door" and 'key' not in inv and door == 0:
            print("The door is locked")
        if user_input.lower() == "open door" and 'key' in inv or user_input.lower() == "use key" and 'key' in inv or user_input.lower() == "open key with door" and 'key' in inv or user_input.lower() == "use the key" and 'key' in inv:
            print("The door is unlocked")
            door = 1
       
        if user_input.lower() == "open window":
            print("Opening the window is not possible.")
       
        # Screwdriver options
        if user_input.lower() == "use screwdriver" and 'screwdriver' in inv:
            print("This does nothing")
        if user_input.lower() == "use screwdriver" and 'screwdriver' not in inv:
            print("You are not carrying a screwdriver")


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



