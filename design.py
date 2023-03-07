# Designet i tkinter, der skal visualisere placeringer i historien
import tkinter as tk
import pygame.image
from pygame.locals import *

# Initialize pygame
pygame.init()

# Create a window
window = tk.Tk()
window.title("Display of locations in the game")

# Create an entry widget for user input
user_input = tk.Entry(window)
user_input.pack()

# Load the images
image1 = pygame.image.load("middle.png")
image2 = pygame.image.load("north.png")
image3 = pygame.image.load("south.png")
image4 = pygame.image.load("east.png")
image5 = pygame.image.load("west.png")

# Define a function to display the image
def display_image():
    
    # Middle
    if user_input.get().lower() == "middle":
        # Create a Pygame display surface
        screen = pygame.display.set_mode(image1.get_size())
        # Blit the image onto the display surface
        screen.blit(image1, (0, 0))
        # Update the display
        pygame.display.update()

    # North
    if user_input.get().lower() == "north":
        # Create a Pygame display surface
        screen = pygame.display.set_mode(image2.get_size())
        # Blit the image onto the display surface
        screen.blit(image2, (0, 0))
        # Update the display
        pygame.display.update()

    # South
    if user_input.get().lower() == "south":
        # Create a Pygame display surface
        screen = pygame.display.set_mode(image3.get_size())
        # Blit the image onto the display surface
        screen.blit(image3, (0, 0))
        # Update the display
        pygame.display.update()

    # East
    if user_input.get().lower() == "east":
        # Create a Pygame display surface
        screen = pygame.display.set_mode(image4.get_size())
        # Blit the image onto the display surface
        screen.blit(image4, (0, 0))
        # Update the display
        pygame.display.update()

    # West
    if user_input.get().lower() == "west":
        # Create a Pygame display surface
        screen = pygame.display.set_mode(image5.get_size())
        # Blit the image onto the display surface
        screen.blit(image5, (0, 0))
        # Update the display
        pygame.display.update()

# Create a button to display the image
display_button = tk.Button(window, text="Display Image", command=display_image)
display_button.pack()

# Start the Tkinter event loop
window.mainloop()

# Quit pygame
pygame.quit()
