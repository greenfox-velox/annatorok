aa = [1, 2, 3]
out = 0
# if the aa list contains one element set the out to 1
# if the aa list contains two element set the out to 2
# if the aa list contains more than 2 set the out to 10
# if the aa contains no elements it should set to -1

lenaa = len(aa)

if lenaa == 0:
    out = -1
elif lenaa > 2:
    out = 10
else:
    out = lenaa

print(out)


'''
if len(aa) == 0:
    out = -1
elif len(aa) == 1 or len(aa) == 2:
    out = len(aa)
else:
    out = 10

print(out)



if len(aa) == 0:
    out = -1
elif len(aa) == 1:
    out = 1
elif len(aa) == 2:
    out = 2
else:
    out = 10

print(out)

if len(aa) == 1:
    out = 1
elif len(aa) == 2:
    out = 2
elif len(aa) > 2:
    out = 10
elif len(aa) == 0:
    out = -1
print(out)
'''
