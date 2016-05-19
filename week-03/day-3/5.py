# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack:

    def __init__(self):
        self.elements = []

    def size(self):
        x = 0
        for element in self.elements:
            x += 1
        return x

    def push(self, num):
        self.elements = self.elements + [num]

    def pop(self):
        list = self.elements[-1]
        self.elements = self.elements[:-1]
        return list

stackA = Stack()

stackA.push(1)
stackA.push(5)
stackA.push(8)
stackA.push(13)
print(stackA.elements)
print(stackA.pop())
print(stackA.elements)
