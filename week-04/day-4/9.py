# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def string(n):
    if len(n) <= 1:
        return n[0]
    else:
        return n[0] + '*' + string(n[1:])

print(string('eraxalmxxayyyy'))


# def string(n):
#     if len(n) <= 1:
#         return n
#     else:
#         if n[0] == 'x':
#             return 'y' + string(n[1:])
#         else:
#             return n[0] + string(n[1:])
#
# print(string('eraxalmxxayyyy'))
