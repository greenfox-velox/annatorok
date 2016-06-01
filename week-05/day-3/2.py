# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def number_of_lines(filename):
    try:
        f = open(filename)
        text = f.readlines()
        f.close()
        lines = 0
        for line in text:
            lines += 1
        return lines
    except FileNotFoundError:
        return 0

print(number_of_lines('file.txt'))
