# Lobby #
import random

### look
# Definitioner af variabler:
room = 1
leaflet = False
location = 0
inv = []

# Inputs
while True: # while is running:
    user_input = input(" ")

    if user_input == "look":
        if room == 1: # lobby
            # Location: middle [0]
            if location == 0 and leaflet != True or leaflet in inv:
                print("The Lobby")
                print("You are standing in a lobby, there is a leaflet on the coffee table.")
                print("There is a door in the south direction.")
            elif location == 0:
                print("The Lobby")
                print("You are standing in a lobby.")
                print("There is a door in the south direction.")
    else:
        print("I beg your pardon?")

