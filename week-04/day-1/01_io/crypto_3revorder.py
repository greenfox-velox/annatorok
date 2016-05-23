# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name, 'r')
    text = f.readlines()
    rev_order_list = ''
    new_List = text[::-1]
    for x in new_List:
        rev_order_list += x
    f.close()
    return rev_order_list
