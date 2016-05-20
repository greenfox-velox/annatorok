# output = create_palindrome('pear')
#
# print(output) # it prints: pearraep

def create_palindrome():
    string = input('Please enter a word: ')
    string2 = string + string[::-1]
    return string2

print(create_palindrome())
