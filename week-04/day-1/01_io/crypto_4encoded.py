# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    decoded_list = ''
    for x in text:
        if x != '\n' or x != ' ':
            decoded_list += x
        else:
            decoded_list += chr(ord(x)-1)
    f.close()
    return decoded_list
