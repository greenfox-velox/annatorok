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

    def __init__(self, canvas):
        self.canvas = canvas
        self.m = []
        # self.m.append(self.hero)

    def create_matrix_element(self, tile_map, rows, columns):
        for x in range(rows):
            for y in range(columns):
                self.create_matrix_for_gameboard(tile_map, y, x)

    def create_matrix_for_gameboard(self,tile_map, y, x):
        if tile_map[y][x] == 0:
            self.m.append(Floor(self.canvas, x, y))
        else:
            self.m.append(Wall(self.canvas, x, y))

    def draw_gameboard(self):
        self.create_matrix_element(tile_map, rows, columns)
        for i in self.m:
            i.draw()

    # def draw_hero(self):
    #     self.hero.draw_char()

    # def key(self,key):
    #     # Movement = W-A-S-D Attack = Space
    #     press = key
    #     if press == 'w':
    #
    #     if press == 's':
    #
    #     if press == 'a':
    #
    #     if press == 'd':
    #
    #     if press == 'space':
    #         self.attack()
