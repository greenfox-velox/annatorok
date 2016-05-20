# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print ("Hello ", self.first_name + self.last_name)


class Student(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # self.first_name = first_name
        # self.last_name = last_name
        self.grades = []


    def add_grade(self, grade):
        self.grades.append(grade)
        # self.grades = self.grades + [grade]

    def salute(self):
        self.greet()
        total = 0
        for x in self.grades:
            total = total + x
        print(total / len(self.grades))


anna = Person("Anna ", "Török")
anna.greet()

aladar = Student("Aladar ", "Kovago")
aladar.add_grade(1)
aladar.add_grade(2)
aladar.add_grade(3)
aladar.add_grade(4)
aladar.salute()
