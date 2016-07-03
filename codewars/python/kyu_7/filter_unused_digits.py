# Given few numbers, you need to print out the digits that are not being used.
#
# Example:
#
# unused_digits(12, 34, 56, 78) # "09"
# unused_digits(2015, 8, 26) # "3479"
# Note:
#
# Result string should be sorted
# The test case won't pass Integer with leading zero

#
# digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# def unused_digits(*args):
#     new_list = ''
#     for x in args:
#         new_list += str(x)
#     for y in new_list:
#         if y in digits:
#             digits.remove(y)
#     return ''.join(digits)
#
# print(unused_digits(2015, 8, 26))

def unused_digits(*args):
    new_list = ''
    for x in range(10):
        if str(x) not in str(args):
            new_list += str(x)
    return ''.join(new_list)

print(unused_digits(123, 50))
