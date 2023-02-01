# Designet i tkinter, der skal visualisere placeringer i historien
import random
import time
import pygame as pg
import tkinter as tk

from design import Design

root = tk.Tk()
w = root.winfo_height
root.geometry("400x400+500+400")

lab1 = tk.Label(root,
    text = "Mariehøne",
    font = "Arial 30")

lab1.pack()

root.mainloop()

class Design:
    def __init__(self) -> None:
        pass