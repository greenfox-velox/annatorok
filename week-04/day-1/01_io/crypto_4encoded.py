# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    decoded_list = ''
    for x in text:

    f.close()
    return decoded_list    
