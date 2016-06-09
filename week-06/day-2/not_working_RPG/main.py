from game import *
from tile import *
from game_map import *
from stats import *
from char import *

def main():

    master = Tk()
    canvas = Canvas(master, width = 1000, height = 720)

    game = Game(canvas)
    game.draw_all()

    master.bind('<KeyPress>', game.keyPressed)

    canvas.pack()
    master.mainloop()

main()
