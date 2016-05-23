# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    decoded_list = ''
    for x in text:
        decoded_list += chr(x-1)
    f.close()
    return decoded_list


# needs to work on this!
