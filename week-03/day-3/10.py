# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

def xmas_tree(input):
    star = 1
    space = input
    for row in range(1, input + 1):
        print(' ' * space + '*' * star)
        star += 2
        space -=1


xmas_tree(8)
