# 10. The fibonacci sequence is a famous bit of mathematics, and it happens to
# have a recursive definition. The first two values in the sequence are
# 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the
# previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21
# and so on. Define a recursive fibonacci(n) method that returns the nth
# fibonacci number, with n=0 representing the start of the sequence.

# refact

def fib(n):
    if  n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(10))


# def fib(n):
#     if  n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(4))
# print(fib(5))
# print(fib(10))
