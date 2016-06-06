# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

sentence = 'This website is for losers LOL'

def disemvowel(string):
    vowels = 'aeiouAEIOU'
    new_sentence = ''
    for i in string:
        if i not in vowels:
            new_sentence += i
    return ''.join(new_sentence)


print(disemvowel(sentence))
