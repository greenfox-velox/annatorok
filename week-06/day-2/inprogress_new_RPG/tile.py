from tkinter import *

class Tile():

    def __init__(self, x, y):
        self.tile_size = 72
        self.x = x
        self.y = y
        self.floor_image = PhotoImage(file = 'images/floor.gif')
        self.wall_image = PhotoImage(file = 'images/wall.gif')

    def draw_tile(self, image, canvas):
        canvas.create_image(5 + self.x * self.tile_size, 5 + self.y * self.tile_size, image=image, anchor = NW)

class Floor(Tile):

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, canvas):
        self.draw_tile(self.floor_image, canvas)

class Wall(Tile):

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, canvas):
        self.draw_tile(self.wall_image, canvas)
