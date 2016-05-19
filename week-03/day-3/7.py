# create a function that takes a list and returns a new list with all the elements doubled
list = [1, 2, 3, 4]

def elements_double(input):
        newList = []
        newList = input * 2
        return newList

print(elements_double(list))

def elements_double(input):
        newList = []
        for i in input:
            newList = newList + [(i * 2)]
            # newList.append(i*2)
        return newList

print(elements_double(list))
