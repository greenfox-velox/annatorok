# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.

def anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(anagram('alma', 'mala'))

# Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.

from collections import OrderedDict


def count_letters(string):
    dicts = {}
    for letter in string.lower():
        dicts[letter] = (string.lower()).count(letter)
    return dicts

print(count_letters('lomhamacsKa'))
