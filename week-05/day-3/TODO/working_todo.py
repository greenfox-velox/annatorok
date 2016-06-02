import sys
import csv

class Todo():

    def __init__(self):
        self.file_name = 'todo_list.csv'

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

    def controller_l(self):
        if len(sys.argv) == 2:
            print(self.load_list())
        else:
            print('Too many arguments were given, only give 1!')

    def controller_a(self):
        if len(sys.argv) == 2:
            print('Unable to add: No task is provided')
        else:
            self.add_to_list(sys.argv[2])

    def controller_c(self):
        if len(sys.argv) == 2:
            print('Unable to check: No index is provided')
        else:
            self.check_task()

    def controller_r(self):
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
                self.controller_l()
            elif sys.argv[1] == '-a':
                self.controller_a()
            elif sys.argv[1] == '-r':
                self.controller_r()
            elif sys.argv[1] == '-c':
                self.controller_c()

    def load_list(self):
        f = open(self.file_name)
        todo_list = csv.reader(f, delimiter = ';')
        output = ''
        number = 1
        for i in todo_list:
            output += (str(number) + ' - ' + self.checked_or_not(i[0]) + ' '+ i[1] + '\n')
            number += 1
        f.close()
        if output == '':
            return 'No todos for today! :)'
        else:
            return output

    def add_to_list(self, new_todo_element):
        f = open(self.file_name, 'a')
        f.write('False;' + new_todo_element + '\n')
        f.close()

    def checked_or_not(self, x):
        if x == 'True':
            return '[x]'
        else:
            return '[ ]'

    def check_task(self):
        f = open(self.file_name)
        check_task = csv.reader(f, delimiter = ';')
        output = []
        try:
            for i in check_task:
                output.append(i)
            if output[int(sys.argv[2])-1][0] == 'False':
                    output[int(sys.argv[2])-1][0] = 'True'
            f.close()
            f = open(self.file_name, 'w')
            for i in output:
                f.write(i[0] + ';' + i[1] + '\n')
            f.close()
        except ValueError:
                print('Unable to check: Index is not a number')
        except IndexError:
                print('Unable to check: Index is out of bound')

    def remove_from_list(self, remove_n_task):
        f = open(self.file_name)
        remove_line = f.readlines()
        try:
            remove_line.remove(remove_line[int(remove_n_task)-1])
        except ValueError:
                print('Unable to remove: Index is not a number')
        except IndexError:
                print('Unable to remove: Index is out of bound')
        f.close()
        f = open(self.file_name, 'w')
        for i in remove_line:
            f.write(i)
        f.close()

    def create_file(self):
        try:
            f = open(todo_list+'.'+csv, 'a')
            f.close()
        except FileNotFoundError:
            return 'File does not exists!'

    def missing_file(self):
        try:
            f = open(self.file_name, 'a')
            f.close()
        except FileNotFoundError:
            self.create_file()


todo = Todo()
todo.main()
