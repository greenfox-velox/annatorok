numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function


def sum_of_numbers(input):
    total = 0
    for i in input:
        total = total + i
    return total

print(sum_of_numbers(numbers))
