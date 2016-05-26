# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).


def squared(n1, n2):
    if n1 == 0:
        return 0
    elif n2 == 0
        return 1
    else:
        return squared(n1, n2-1) * n1


print(squared(3,2))


# def power(i, j):
#     square = i ** j
#     return square
#
# print(power(3,4))
