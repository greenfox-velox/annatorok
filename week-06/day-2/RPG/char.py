from tkinter import *
from gameboard import tile_map

class Character():
    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.tile_size = 72
        self.x = x
        self.y = y
        self.health = 100
        self.level = 1
        self.score = 0

    def create_char(self, image):
        self.canvas.create_image(5 + self.x * self.tile_size, 5 + self.y * self.tile_size, image=image, anchor = NW)

class Hero(Character):
    def __init__(self, canvas, x, y, tile_map):
        super().__init__(canvas,x, y)
        self.hero_image = PhotoImage(file = 'images/hero-down.gif')
        self.tile_map = tile_map

    def draw_char(self):
        self.create_char(self.hero_image)

    def move_down(self, event):
        if self.tile_map[self.y+1][self.x] == 0:
            self.hero_image = PhotoImage(file = 'images/hero-down.gif')
            if self.y < 9:
                self.y += 1
            self.draw_char()

    def move_up(self, event):
        if self.tile_map[self.y-1][self.x] == 0:
            self.hero_image = PhotoImage(file = 'images/hero-up.gif')
            if self.y > 0:
                self.y = self.y - 1
            self.draw_char()

    def move_right(self, event):
        if self.tile_map[self.y][self.x+1] == 0:
            self.hero_image = PhotoImage(file = 'images/hero-right.gif')
            if self.x < 9:
                self.x = self.x + 1
            self.draw_char()

    def move_left(self, event):
        if self.tile_map[self.y][self.x-1] == 0:
            self.hero_image = PhotoImage(file = 'images/hero-left.gif')
            if self.x > 0:
                self.x = self.x - 1
            self.draw_char()

    # def attack(self):

class Boss(Character):

    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)
        self.boss_image = PhotoImage(file = 'images/boss.gif')

    def draw_char(self):
        self.create_char(self.boss_image)

class Skeleton(Character):
    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)
        self.skeleton_image = PhotoImage(file = 'images/skeleton.gif')

    def draw_char(self):
        self.create_char(self.skeleton_image)
