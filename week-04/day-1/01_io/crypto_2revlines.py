# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name, 'r')
    text = f.readlines()
    new_List = ''
    for x in text:
        x = x.rstrip()
        reverse_line = x[::-1]
        new_List += reverse_line + '\n'
    f.close()
    return new_List
