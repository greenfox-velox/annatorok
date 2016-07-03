# The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples:
#
# "din" => "((("
#
# "recede" => "()()()"
#
# "Success" => ")())())"
#
# "(( @" => "))(("




from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    new_string = ''
    count = Counter(word)
    for x in word:
        if count[x] == 1:
            new_string += '('
        else:
            new_string += ')'
    return new_string

print(duplicate_encode('recede'))
