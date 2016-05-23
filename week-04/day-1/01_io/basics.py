# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    f = open(file_name, 'r')
    text = f.read()
    f.close()
    return text

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    for line in range(number):
        text = f.readline()
    f.close()
    return text.rstrip()

# def readline(file_name, number):
#     f = open(file_name)
#     text = f.readlines()[number-1].rstip()
#     f.close()
#     return text


# print(readline('texts/zen_of_python.txt', 2))

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    word = sentence.strip('.').split()
    return word


# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    words2 = ' '.join(words)
    words2 = words2 + '.'
    return words2

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    new_List = []
    for x in string:
        new_List.append(ord(x))
    return new_List

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
        character_c = ''
        for x in char_codes:
            character_c += chr(x)
        return character_c
