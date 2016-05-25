from tkinter import *

# create a 300x300 canvas.
# draw its diagonals in green.

master = Tk()

canvas = Canvas(master, width='300', height='300')
canvas.pack()

diagonal = canvas.create_line(0, 0, 300, 300, fill='green')


master.mainloop()
