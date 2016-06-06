# Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.
#
# For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"


def order(sentence):
    new_list = []
    lista = sentence.split()
    for x in range(1, len(lista)+1):
        for y in range(len(lista)):
            if str(x) in lista[y]:
                new_list.append(lista[y])
            else:
                pass
    sentence = ' '.join(new_list)
    return sentence

print(order('is2 Thi1s T4est 3a'))

# def order(sentence):
#   numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#   words_list = sentence.split(' ')
#   new_list = []
#   new_sentence = ''
#   for num in numbers:
#       for word in words_list:
#           if str(num) in word:
#               new_list.append(word)
#               new_sentence = ' '.join(new_list)
#   return new_sentence


# def order(sentence):
#   # code here
#     number_order = []
#     sentence = sentence.split()
#     for word in sentence:
#         for letter in word:
#             if letter.isdigit():
#                 number_order.append(int(letter))
#     output = ''
#     for n in range(1,10):
#         if n in number_order:
#             output += sentence[number_order.index(n)]
#             output += ' '
#     return output.strip()
