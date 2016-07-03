from char import *
from game_map import *
from tile import *
from stats import *

class Game():

    def __init__(self, canvas):
        self.canvas = canvas
        self.hero = Hero(0, 1)
        self.game_map = Map()
        self.boss = Boss(0, 5)
        self.skeleton = Skeleton(6, 8)
        self.skeleton2 = Skeleton(0, 7)
        self.skeleton3 = Skeleton(4, 5)
        self.stat = Stat(self.hero)

    def keyPressed(self, event):
        next_x = self.hero.x
        next_y = self.hero.y
        if event.keysym == 'Down':
                next_y += 1
        elif event.keysym == 'Right':
                next_x += 1
        elif event.keysym == 'Left':
                next_x -= 1
        elif event.keysym == 'Up':
                next_y -= 1
        if self.game_map.check_edge(next_x, next_y) and self.game_map.check_floor(next_x, next_y):
            self.hero.move(next_x, next_y, self.hero.images[event.keysym])
            self.hero.draw_all()


    def draw_all(self):
        self.game_map.draw_tile(self.canvas)
        self.hero.draw_char(self.canvas)
        self.boss.draw_char(self.canvas)
        self.skeleton.draw_char(self.canvas)
        self.skeleton2.draw_char(self.canvas)
        self.skeleton3.draw_char(self.canvas)
        self.stat.draw_text(self.canvas)
