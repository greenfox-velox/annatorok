ah = ['kuty', 'macsk', 'cic']
# add to all elements an 'a' on the end

i = 0

while i < len(ah):
    ah[i] = ah[i] + "a"
    i += 1

# while i < len(ah):
#     print(ah[i] + "a")
#     i += 1

for i in ah:
    print(i + "a")

for i in range(len(ah)):
    ah[i] += "a"

print(ah)
