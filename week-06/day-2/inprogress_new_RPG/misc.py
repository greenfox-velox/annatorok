# for row in range(rows):
#     for column in range(columns):
#         if tile_map[column][row] == 0:
#             canvas.create_image(row * tile_size, column * tile_size, image=floor, anchor = NW)
#         else:
#             canvas.create_image(row * tile_size, column * tile_size, image=wall, anchor = NW)
# canvas.create_image(0, 0, image=hero, anchor = NW)

# class Hero_char():
#     def __init__(self):
# hero = PhotoImage(file = 'hero-down.gif')
    # def hero_char():
    #     self.canvas.create_image(0, 0, image=hero, anchor = NW)

#
#
# root = Tk()
# tile = NotEmptyTile()
# root.mainloop()



# master = Tk()
# rows = 10
# columns = 10

# canvas_size = 720
# tile_size = 72

#
# canvas = Canvas(master, width = canvas_size, height = canvas_size)
# canvas.pack()
#
# floor = PhotoImage(file = 'floor.gif')
# wall = PhotoImage(file = 'wall.gif')
# hero = PhotoImage(file = 'hero-down.gif')
#
# tile_map = ([0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
#             [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
#             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#             [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
#             [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
#             [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
#             [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
#             [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
#             [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
#             [0, 1, 0, 1, 0, 1, 0, 0, 0, 0])
#
# def create_area(tile_map):
#     for row in range(rows):
#         for column in range(columns):
#             floor_or_wall(column, row)
#
# def floor_or_wall(column, row):
#     if tile_map[column][row] == 0:
#         canvas.create_image(row * tile_size, column * tile_size, image=floor, anchor = NW)
#     else:
#         canvas.create_image(row * tile_size, column * tile_size, image=wall, anchor = NW)
#
# def hero_char():
#     canvas.create_image(0, 0, image=hero, anchor = NW)
