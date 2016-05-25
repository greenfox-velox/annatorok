from tkinter import *

# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

master = Tk()

canvas = Canvas(master, width='300', height='300', bg='black')
canvas.pack()

red_line = canvas.create_line(0, 150, 300, 150, fill='red')
green_line = canvas.create_line(150, 0, 150, 300, fill='green')


master.mainloop()
