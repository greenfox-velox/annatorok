# Create a function called shortcut to remove all the lowercase vowels in a given string.
#
# Examples
#
# shortcut("codewars") # --> cdwrs
# shortcut("goodbye")  # --> gdby
# Don't worry about uppercase vowels.


def shortcut( s ):
    vowels = 'aeiou'
    new_string = ''
    for x in s:
        if x not in vowels:
            new_string += x
    return new_string
