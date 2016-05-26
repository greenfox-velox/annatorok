# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

def sum_of_digits(n):
    if n <= 10:
        return n
    else:
        return (n%10) + sum_of_digits(n//10)

print(sum_of_digits(3289))

# with for loop
# def sum_of_digits(n):
#     total = 0
#     for i in str(n):
#         total += int(i)
#
#
# sum_of_digits(938)

# def sum(number):
#     if number < 10:
#         return number
#     else:
#         last_digit = number % 10
#         rest_of_num = number // 10
#         return last_digit + sum(rest_of_num)
#
# print(sum(12345))
