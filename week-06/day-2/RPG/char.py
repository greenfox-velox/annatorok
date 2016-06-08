from tkinter import *

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
    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)
        self.hero_up = PhotoImage(file = 'images/hero-up.gif')
        self.hero_down = PhotoImage(file = 'images/hero-down.gif')
        self.hero_left = PhotoImage(file = 'images/hero-left.gif')
        self.hero_right = PhotoImage(file = 'images/hero-right.gif')

    def draw_char(self):
        self.create_char(self.hero_down)

    def move_down(self, event):
        self.y += 1
        self.create_char(self.hero_down)

    def move_up(self, event):
        self.y = self.y - 1
        self.create_char(self.hero_up)

    def move_right(self, event):
        self.x = self.x + 1
        self.create_char(self.hero_right)

    def move_left(self, event):
        self.x = self.x - 1
        self.create_char(self.hero_left)

    # def attack(self):

class Boss(Character):

    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)
        self.boss = PhotoImage(file = 'images/boss.gif')
        # self.image_up = PhotoImage(file = 'hero-up.gif')
        # self.image_down = PhotoImage(file = 'hero-down.gif')
        # self.image_left = PhotoImage(file = 'hero-left.gif')
        # self.image_right = PhotoImage(file = 'hero-right.gif')

    def draw_char(self):
        self.create_char(self.boss)

# class Skeleton(Character):
    # def __init__(self, canvas, x, y):
    #     super().__init__(canvas,x, y)
    #     self.skeleton = PhotoImage(file = 'images/skeleton.gif')
    #     # self.image_up = PhotoImage(file = 'hero-up.gif')
    #     # self.image_down = PhotoImage(file = 'hero-down.gif')
    #     # self.image_left = PhotoImage(file = 'hero-left.gif')
    #     # self.image_right = PhotoImage(file = 'hero-right.gif')
    #
    # def draw_char(self):
    #     self.create_char(self.skeleton)
