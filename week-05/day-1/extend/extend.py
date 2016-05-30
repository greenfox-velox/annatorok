# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    pool = sorted(pool)
    if len(pool) % 2 != 0:
         return pool[int((len(pool)-1)/2)]
    else:
        return (pool[int(len(pool)/2)-1] + pool[int(len(pool)/2)])/2

# Returns true if the param is a vowel
def is_vovel(char):
    if char in 'aeiou':
        return True
    else:
        return False

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    new = ''
    for char in teve:
        if is_vovel(char):
            new += char + 'v' + char
        else:
            new += char
    return result
