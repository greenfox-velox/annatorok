# Create a function which answers the question "Are you playing Banjo?". If your name starts with the letter "R" or lower case "r", you are playing Banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:

# name + "plays banjo" name + "does not play banjo"

# def areYouPlayingBanjo(name):
#     for x in name:
#         if x[0] == 'R' or x[0] == 'r':
#             return name + ' plays banjo'
#         else:
#             return name + ' does not play banjo'

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

print(areYouPlayingBanjo('Anna'))
