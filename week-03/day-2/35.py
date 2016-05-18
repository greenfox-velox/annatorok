# create a function that returns it's input factorial

def factorial(input):
    factor = 1
    for i in range(1, input+1):
        factor = factor * i
    return factor

print(factorial(5))
