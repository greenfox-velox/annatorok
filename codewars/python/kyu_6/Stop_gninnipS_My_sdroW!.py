# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
#
#
# Examples:
#
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

sentence = 'Hey fellow warriors'

def spin_words(sentence):
    sentence = sentence.split(' ')
    new_string = []
    for i in sentence:
        if len(i) < 5:
            i = i
            new_string += [i]
        else:
            i = i[::-1]
            new_string += [i]
    return ' '.join(new_string)

print(spin_words(sentence))
