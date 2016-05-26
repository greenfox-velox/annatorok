# 6. We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or
# multiplication).

# ears = 0
# for i in range(123):
#     if i % 2 == 0:
#         ears += 3
#     else:
#         ears += 2
# print(ears)

def bunny_ears(n):
    if n <= 1:
        return 2
    else:
        if (n-1)%2 == 0:
            return bunny_ears(n-1) + 2
        else:
            return bunny_ears(n-1) + 3

# print(bunny_ears(58))

print(bunny_ears(1))
print(bunny_ears(2))
print(bunny_ears(3))
print(bunny_ears(4))
print(bunny_ears(5))


# def bunny(n):
#     if n <= 0:
#         return 0
#     else:
#         return bunny(n-1) + 2
#
# print(bunny(8))
