# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

# ears(n-1) + 2
#
# def total(n):

def bunny(n):
    if n <= 1:
        return 2
    else:
        return bunny(n-1) + 2

print(bunny(8))

# ears = 0
# for i in range(123):
#     ears += 2
#
# print(ears)
