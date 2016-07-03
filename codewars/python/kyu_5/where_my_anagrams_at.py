# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
#
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
#
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):
    anagram_array = []
    for x in words:
        if sorted(x) == sorted(word):
            anagram_array.append(x)
    return anagram_array

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
