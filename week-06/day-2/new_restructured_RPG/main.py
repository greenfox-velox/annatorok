from tkinter import *
from game import Game
from tile import Tile, Floor, Wall
from game_map import Map
from stats import Stat
from char import Character, Hero, Boss, Skeleton

def main():

    master = Tk()
    canvas = Canvas(master, width = 1000, height = 720)

    game = Game(canvas)
    game.draw_all()

    master.bind('<KeyPress>', game.keyPressed)

    canvas.pack()
    master.mainloop()

main()
