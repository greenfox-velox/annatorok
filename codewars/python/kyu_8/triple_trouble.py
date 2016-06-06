# Create a function that will return a string that combindes all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!
#
# Ex) Input: "aa", "bb" , "cc" => Output: "abcabc"

a = 'burn'
b = 'reds'
c = 'rolls'

def triple_trouble(one, two, three):
    new_list = ''
    for i in range(len(a)):
        new_list += a[i] + b[i] + c[i]
    return new_list

print(triple_trouble(a,b,c))
