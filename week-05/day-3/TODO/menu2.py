

print('==============================')
print('      TODO APPLICATION        ')
print('                              ')
print('            MENU              ')
print('                              ')
print(' 1. -l Lists all the tasks    ')
print(' 2. -a Adds a new tasks       ')
print(' 3. -r Removes a task         ')
print(' 4. -c Completes a task       ')
print(" 5. Exit from the application ")
print('                              ')
print('==============================')


def menu():

    try:
        user_input = int(input('Please choose what you want to do: '))
        if user_input == 1:
            print('You chose: List all the tasks')
        if user_input == 2:
            print('You chose: Add a new tasks')
        if user_input == 3:
            print('You chose: Remove a task')
        if user_input == 4:
            print('You chose: Complete a task')
        if user_input == 5:
            exit()
    except ValueError:
        print('Please choose a number between 1 to 5 instad of a word')


while True:
    menu()
