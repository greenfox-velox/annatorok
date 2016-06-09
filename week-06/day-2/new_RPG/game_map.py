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

class Map():

    def __init__(self):
        self.map = []
        self.tile_map = tile_map

    def create_matrix_element(self, rows, columns):
        for x in range(rows):
            for y in range(columns):
                self.create_matrix_for_map(x, y)

    def create_matrix_for_map(self, x, y):
        if self.tile_map[y][x] == 0:
            self.map.append(Floor(x, y))
        else:
            self.map.append(Wall(x, y))

    def draw_tile(self, canvas):
        self.create_matrix_element(rows, columns)
        for tile in self.map:
            tile.draw(canvas)

    def check_edge(self, x, y):
        return y <= 9 and y >= 0 and x >= 0 and x <= 9

    def check_floor(self, x, y):
        return self.tile_map[y][x] == 0
