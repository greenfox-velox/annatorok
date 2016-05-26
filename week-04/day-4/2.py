# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def summa(n):
    if n <= 0:
        return 0
    else:
        return summa(n-1) + n

print(summa(4))



# def concat(n):
#     if n <= 0:
#         return []
#     else:
#         return concat(n-1) + [n]
#
#
# print(concat(6))
