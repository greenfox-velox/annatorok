# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

# n = 'eraxalmxxayyyy'
#
# output = ''
# for i in n:
#     if i == 'x':
        # i = 'y'
#         output += i
#     else:
#         output += i
#
# print(output)

def string(n):
    if len(n) <= 1:
        return n
    else:
        if n[0] == 'x':
            return 'y' + string(n[1:])
        else:
            return n[0] + string(n[1:])

print(string('eraxalmxxayyyy'))
