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

    def __init__(self, canvas, hero):
        self.canvas = canvas
        self.m = []
        self.hero = hero

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

    def keyPressed(self, event):
        if event.keysym == 'Down':
            self.hero.move_down()
        if event.keysym == 'Right':
            self.hero.move_right()
        if event.keysym == 'Left':
            self.hero.move_left()
        if event.keysym == 'Up':
            self.hero.move_up()

class Stat():

    def __init__(self, canvas, hero):
        self.canvas = canvas
        self.hero = hero
        self.x = 760
        self.y = 100

    def draw_text(self):
        self.stat = self.hero.name + '(Level ' + str(self.hero.level) + ') HP: ' + str(self.hero.hp) + '/' + str(self.hero.max_hp) + ' | DP: ' + str(self.hero.dp) + ' | SP: ' + str(self.hero.sp)
        self.canvas.create_text(self.x, self.y, text = self.stat)
