from tile import *
from gameboard import *
from char import *

def main():
    
    master = Tk()
    canvas = Canvas(master, width = 1000, height = 720)

    hero = Hero(0, 1, canvas, tile_map)

    game = Gameboard(canvas, hero)
    game.draw_gameboard()
    stat = Stat(canvas, hero)
    stat.draw_text()
    hero.draw_char()

    boss = Boss(0, 5, canvas)
    boss.draw_char()

    skeleton = Skeleton(6, 8, canvas)
    skeleton.draw_char()

    skeleton2 = Skeleton(0, 7, canvas)
    skeleton2.draw_char()

    skeleton3 = Skeleton(4, 5, canvas)
    skeleton3.draw_char()

    master.bind('<KeyPress>', game.keyPressed)

    canvas.pack()
    master.mainloop()

main()
