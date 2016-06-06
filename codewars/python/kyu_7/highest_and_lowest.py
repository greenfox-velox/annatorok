# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#
# Example:
#
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes:
#
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

# def high_and_low(numbers):
#   numbers = numbers.split()
#   for elm in range(len(numbers)):
#     numbers[elm] = int(numbers[elm])
#   return str(max(numbers)) + ' ' + str(min(numbers))

def high_and_low(numbers):
    new_list = numbers.split(' ')
    highest = new_list[0]
    for i in new_list:
        if int(i) > int(highest):
            highest = i
    lowest = new_list[0]
    for j in new_list:
        if int(j) < int(lowest):
            lowest = j
    output = [highest, lowest]
    return str(' '.join(output))

print(high_and_low('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'))
