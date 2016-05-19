# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student:

    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        if grade <= 5 and grade > 0:
            self.grades = self.grades + [grade]

    def get_average(self):
        total = 0
        for x in self.grades:
            total += x
        return total / len(self.grades)

StudentA = Student()

StudentA.add_grade(2)
StudentA.add_grade(5)
StudentA.add_grade(1)
StudentA.add_grade(4)
print(StudentA.get_average())
