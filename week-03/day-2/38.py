numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)



def find_minimum(input):
    mininum = input[0]
    for i in input:
        if i < mininum:
            mininum = i
    return mininum

print(find_minimum(numbers))
