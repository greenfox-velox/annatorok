# In Python, lists will be represented by a preloaded LinkedList class with the members value and next. Here's an example:
#
# LinkedList(1, LinkedList(2, LinkedList(3)))
# Write a function listToArray (or list_to_array in Python) that converts a list to an array, like this:
#
# [1, 2, 3]
# Assume all inputs are valid lists with at least one value. For the purpose of simplicity, all values will be either numbers, strings, or Booleans.

def list_to_array(lst):
    new_list=[]
    while lst:
        new_list.append(lst.value)
        lst=lst.next
    return new_list
