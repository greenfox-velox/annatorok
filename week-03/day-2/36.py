numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list
#
# def reverse(numbers):
#     for i in numbers:
#         newNumbers = []
#         newNumbers = numbers[::-1]
#     print(newNumbers)
#
# reverse(numbers)


numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def revert(input):
    reverse = []
    for i in range(len(input)-1, -1, -1):
        reverse = reverse + [input[i]]
    return reverse

print(revert(numbers))
