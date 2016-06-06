# Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:
#
# multiply(3)==15
# multiply(10)==250

def multiply(n):
    result = n * (5**len(str(n)))
    return result

print(multiply(-2))
