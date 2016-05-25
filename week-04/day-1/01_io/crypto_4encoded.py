# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    decoded_list = ''
    for x in text:
        if x != '\n' or x != ' ':
            decoded_list += x
        else:
            char_code = ord(x)
            shift_with_one_char = char_code - 1
            prev_char = chr(shift_with_one_char)
            decoded_list += prev_char

            # decoded_list += chr(ord(x)-1)
    f.close()
    return decoded_list


# def decrypt(file_name):
#     f = open(file_name)
#     text = f.read()
#     decoded_list = ''
#     for x in text:
#         if x != '\n' or x != ' ':
#             decoded_list += x
#         else:
#            decoded_list += chr(ord(x)-1)
#     f.close()
#     return decoded_list
