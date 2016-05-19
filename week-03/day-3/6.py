# create a function that takes a list and returns a new list that is reversed
list = [1, 2, 3, 4]

def reverse_list(input):
    newList = []
    for x in input:
        newList = input[::-1]

    return newList

print(reverse_list(list))
