 Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def diamond(row):
    star = 1
    spaces = row
    for x in range(1,row+1):
        print(' ' * spaces + '*' * star)
        star += 2
        spaces -= 1
    for x in range(row, -1, -1):
        print(' ' * spaces + '*' * star)
        star -= 2
        spaces += 1

diamond(6)
