# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def triangle(row):
    for stars in range(1, row + 1):
        print("*" * stars)

triangle(7)

def triangle(number):
    star = 1
    while star < number:
        print("*" * star)
        star += 1

triangle(7)


def triangle(lines):
    for i in range(lines):
        print('*'*(i+1))

triangle(7)

def triangle(lines):
    for i in range(lines+1):
        print('*' * i)

triangle(7)
