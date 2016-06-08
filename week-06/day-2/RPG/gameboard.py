from tile import *

tile_map = ([0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0])

rows = 10
columns = 10

class Gameboard():

    def __init__(self, canvas, hero, stat):
        self.canvas = canvas
        self.m = []
        self.hero = hero
        self.stat = hero.stat

    def create_matrix_element(self, tile_map, rows, columns):
        for x in range(rows):
            for y in range(columns):
                self.create_matrix_for_gameboard(tile_map, x, y)

    def create_matrix_for_gameboard(self,tile_map, x, y):
        if tile_map[y][x] == 0:
            self.m.append(Floor(self.canvas, x, y))
        else:
            self.m.append(Wall(self.canvas, x, y))

    def draw_gameboard(self):
        self.create_matrix_element(tile_map, rows, columns)
        for i in self.m:
            i.draw()

    def draw_text(self, stat):
        self.canvas.create_text(760, 100, x + 200, y + 100, text = self.hero.stat)

    def keyPressed(self, event):
        if event.keysym == 'Down':
            self.hero.move_down()
        if event.keysym == 'Right':
            self.hero.move_right()
        if event.keysym == 'Left':
            self.hero.move_left()
        if event.keysym == 'Up':
            self.hero.move_up()
