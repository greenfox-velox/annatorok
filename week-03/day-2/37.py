numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens


def filter_odds(input):
    evens = []
    for x in input:
        if x % 2 == 0:
            evens = evens + [x]
    return evens

print(filter_odds(numbers))



# def filtering():
#     for x in numbers:
#         evenNumbers = []
#         if numbers[x] % 2 != 0:
#             evenNumbers = evenNumbers + numbers[x]
#             return (evenNumbers)
#
# filtering()
