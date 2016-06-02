import sys

class Todo():

    def __init__(self):
        self.file_name = 'todo_list.txt'

    def main_menu(self):
        print('                           ')
        print('===========================')
        print('                           ')
        print('      TODO APPLICATION     ')
        print('                           ')
        print('   Command line arguments: ')
        print('                           ')
        print(' -l Lists all the tasks    ')
        print(' -a Adds a new tasks       ')
        print(' -r Removes a task         ')
        print(' -c Completes a task       ')
        print('                           ')
        print('===========================')

    def ok_argument(self):
        arguments = ['-l', '-a', '-r', '-c']
        if sys.argv[1] not in arguments:
            print('Unsupported argument')
            self.main_menu()

    def argv_is_a(self):
        if len(sys.argv) == 2:
            print('Unable to add: No task is provided')
        else:
            self.add_to_list(sys.argv[2])

    def argv_is_r(self):
        if len(sys.argv) == 2:
            print('Unable to remove: No index is provided')
        else:
            self.remove_from_list(sys.argv[2])


    def main(self):
        self.missing_file()
        if len(sys.argv) == 1:
            self.main_menu()
        else:
            self.ok_argument()
            if sys.argv[1] == '-l':
                print(self.load_list())
            elif sys.argv[1] == '-a':
                self.argv_is_a()
            elif sys.argv[1] == '-r':
                self.argv_is_r()

    def load_list(self):
        try:
            f = open(self.file_name)
            todo_list = f.readlines()
            f.close()
            output = ''
            number = 1
            if len(todo_list) == 0:
                return 'No todos for today! :)'
            else:
                for i in todo_list:
                    output += (str(number) + ' - ' + i)
                    number += 1
                return output
        except FileNotFoundError:
            return 'File does not exists!'


    def add_to_list(self, new_todo_element):
        f = open(self.file_name, 'a')
        f.write(new_todo_element + '\n')
        f.close()

    def remove_from_list(self, remove_n):
        f = open(self.file_name)
        remove_line = f.readlines()
        try:
            if (len(remove_line)) == 1 and remove_n == len(remove_line):
                remove_line.remove(remove_line(0))
            elif (len(remove_line)) < int(remove_n):
                print('Unable to remove: Index is out of bound')
            else:
                remove_line.remove(remove_line[int(remove_n)-1])
        except ValueError:
                print('Unable to remove: Index is not a number')
        f.close()
        f = open(self.file_name, 'w')
        for i in remove_line:
            f.write(i)
        f.close()

    def create_file(self):
        f = open(todo_list+'.'+txt, 'a')

    def missing_file(self):
        try:
            f = open(self.file_name, 'a')
        except FileNotFoundError:
            self.create_file()


todo = Todo()
todo.main()
