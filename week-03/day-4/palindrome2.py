# Create a function that searches for all the palindromes in a string that are at least 3 characters, and returns a list with the found palindromes. Example:
#
# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['og go', ' dad ', 'd d', 'dood', 'eve']

def search_palindrome(string):
    palindrome_list = []
    for i in range(len(string)-2):
        for x in range(3,len(string)):
            if string[i:i+x] == string[i:i+x][::-1]:
                palindrome_list.append(string[i:i+x])
    return palindrome_list

print(search_palindrome('dog goat dad duck doodle never'))
