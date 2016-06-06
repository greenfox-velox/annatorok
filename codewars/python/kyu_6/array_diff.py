# Your goal in this kata is to implement an difference function, which subtracts one list from another.
#
# It should remove all values from list a, which are present in list b.
#
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]

a = [1, 2, 3, 4, 5, 6]
b = [3, 5, 6, 8, 9, 1]

def array_diff(a, b):
    new_list = []
    for i in a:
        if i not in b:
            new_list += [i]
    return new_list

print(array_diff(a, b))
