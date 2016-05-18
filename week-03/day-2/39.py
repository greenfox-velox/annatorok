names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list


def shortest_element(input):
    shortest = input[0]
    for x in input:
        if len(x) < len(shortest):
            shortest = x
    return shortest

print(shortest_element(names))
