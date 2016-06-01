# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divide_by_ten(number):
    try:
        result = 10 / number
        print(result)
    except ZeroDivisionError:
        print('Fail')

divide_by_ten(5)
