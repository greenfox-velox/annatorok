# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    decoded_list = ''
    for x in text:
        if x != '\n' and x != ' ':
            decoded_list += chr(odr(x)-1)
        else:
            decoded_list += x
    f.close()
    return decoded_list


# needs to work on this!
