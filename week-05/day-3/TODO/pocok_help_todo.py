import sys
import csv

class Todo():

    def __init__(self):
        self.file_name = 'todo_list.csv'
        self.missing_file()
        self.open_file()


    def create_file(self):
        f = open('todo_list.csv', 'a')
        f.close()

    def missing_file(self):
        try:
            f = open(self.file_name)
            f.close()
        except FileNotFoundError:
            self.create_file()


    def open_file(self):
        f = open(self.file_name)
        self.todo_list = list(csv.reader(f))
        f.close()
        if len(self.todo_list) == 0:
            return 'No todos for today! :)'
        return self.todo_list

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

    def load_list(self):
        formated_output = []
        for i in range(len(self.todo_list)):
            # formated_output.append(str(i + 1) + '-' + self.todo_list[i][0] + '\n')
            formated_output.append('{} - {}'.format(str(i + 1), self.todo_list[i][0] + '\n'))
        return ''.join(formated_output)

            # output = []
            # number = 1
            # print(todo_list)
            # if todo_list == []:
            #     return 'No todos for today! :)'
            # else:
            #     for i in todo_list:
            #         output += (str(number) + ' - ' + i[0] + '\n')
            #         number += 1
            #     f.close()
            #     return output


    def add_to_list(self, new_todo_element):
        self.todo_list.append('False;' + new_todo_element)

        # f = open(self.file_name, 'a')
        # f.write(new_todo_element)
        # f.close()

    def checked_or_not(self, x):
        if x == True:
            return '[x]'
        else:
            return '[ ]'

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

        # with open('self.file_name', 'w', newline='') as f:
        #     spamwriter = csv.writer(csvfile, delimiter=' ',
        #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        #     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



todo = Todo()
todo.main()
