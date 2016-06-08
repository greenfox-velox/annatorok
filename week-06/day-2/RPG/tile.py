from tkinter import *

class Tile():

    def __init__(self, canvas, x, y):
        self.tile_size = 72
        self.canvas = canvas
        self.x = x
        self.y = y
        self.floor_image = PhotoImage(file = 'images/floor.gif')
        self.wall_image = PhotoImage(file = 'images/wall.gif')

    def draw_tile(self, image):
        self.canvas.create_image(5 + self.x * self.tile_size, 5 + self.y * self.tile_size, image=image, anchor = NW)

class Floor(Tile):

    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)

    def draw(self):
        self.draw_tile(self.floor_image)

class Wall(Tile):

    def __init__(self, canvas, x, y):
        super().__init__(canvas,x, y)

    def draw(self):
        self.draw_tile(self.wall_image)
