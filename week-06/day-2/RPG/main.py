from tile import *
from gameboard import *
from char import *

master = Tk()

#
# hero = PhotoImage(file = 'hero-down.gif')
# hero_up = PhotoImage(file = 'hero-up.gif')
# hero_left = PhotoImage(file = 'hero-left.gif')
# hero_right = PhotoImage(file = 'hero-right.gif')

canvas_size = 720
canvas = Canvas(master, width = canvas_size, height = canvas_size)
canvas.pack()

game = Gameboard(canvas)
game.draw_gameboard()

hero = Hero(0, 1, canvas)
hero.draw_char()

master.bind('<Down>', hero.move_down)
master.bind('<Up>', hero.move_up)
master.bind('<Right>', hero.move_right)
master.bind('<Left>', hero.move_left)


boss = Boss(0, 5, canvas)
boss.draw_char()
# skeleton = Skeleton(0, 2, canvas)
# skeleton.draw_char()


master.mainloop()
