# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def string(n):
    if len(n) <= 1:
        return n
    else:
        output = ''
        if n[0] == 'x':
            return output + string(n[1:])
        else:
            return n[0] + string(n[1:])

print(string('eraxalmxxayyyy'))
