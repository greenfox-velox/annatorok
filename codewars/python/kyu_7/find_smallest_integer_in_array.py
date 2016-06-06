# Find the smallest integer in the array.
#
# Given an array of integers your solution should find the smallest integer. For example:
# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345

def findSmallestInt(arr):
    return min(arr)


# def findSmallestInt(arr):
#     smallest = arr[0]
#     for elem in arr:
#         if elem < smallest:
#             smallest = elem
#     return smallest
