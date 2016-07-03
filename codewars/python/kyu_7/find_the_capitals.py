# Instructions
#
# Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.
#
# Eg. 'CodEWaRs'), [0,3,4,6] )


def capitals(word):
    index_list = []
    i = 0
    for x in word:
        if x == x.upper():
            index_list.append(i)
        i+=1
    return index_list


# def capitals(word):
#     new_list = []
#     for i, x in enumerate(list(word)):
#         if x.isupper():
#             new_list.append(i)
#     return new_list
#
# print(capitals('CodEWaRs'))


# def capitals(word):
#     return [index for index, x in enumerate(word) if x.isupper()]
#
# print(capitals('CodEWaRs'))
