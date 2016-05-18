ag = [3, 4, 5, 6, 7]
# please double all the elements of the list

i = 0
lenag = len(ag)

while i < lenag:
    ag = ag + [ag[i]]
    i += 1

print(ag)


for i in range(lenag):
    ag += [ag[i]]

print(ag)

# while i < len(ag):
#     print(2 * ag[i])
#     i += 1
#
#
# for i in ag:
#     print(2*i)
