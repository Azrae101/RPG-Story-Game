import tkinter as tk

root = tk.Tk()
w = root.winfo_height
root.geometry("400x400+500+400")

lab1 = tk.Label(root,
    text = "Mariehøne",
    font = "Arial 30")

lab1.pack()

root.mainloop()