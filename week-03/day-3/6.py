# create a function that takes a list and returns a new list that is reversed
list = [1, 2, 3, 4]

def reverse_list(input):
    for x in input:
        newList = []
        newList = input[::-1]

    return newList

print(reverse_list(list))
