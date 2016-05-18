ae = 'Jozsi'
# create a function that greets ae

# def greet(name):
#     print("Hello," + name)
#
# greet(ae)


def greet(name):
    return "Hello, " + name

print(greet(ae))

def test(expected, actual):
    if expected == actual:
        print("check")
    else:
        print("JAJ")

test("Hello, Jozsi", greet(ae))
