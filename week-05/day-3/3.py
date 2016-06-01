# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person():

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        if self.birth_date < 0 or self.birth_date > 2016:
            raise ValueError('This is not a valid birth date')

student = Person('Anna', 1986)
student2 = Person('Balint', 2017)


# class Person():
#
#     def __init__(self, name, birth_date):
#         self.name = name
#         self.birth_date = birth_date
#         if self.birth_date < 0 or self.birth_date > 2016:
#             raise ValueError('Not a valid birth year')
#
# try:
# student = Person('Anna', 1986)
# student2 = Person('Balint', 2017)
# except ValueError:
#     print('Not a valid birth year')
