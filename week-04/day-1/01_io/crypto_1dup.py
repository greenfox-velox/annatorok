# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name, 'r')
    text = f.readlines()
    new_List = ''
    for x in text:
        remove_dup = x[::2]
        new_List += remove_dup
    f.close()
    return new_List
