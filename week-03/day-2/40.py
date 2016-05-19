students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10


def get_all_candies_of_under_10(input):
    candy = 0
    for student in input:
        if student['age'] < 10:
            candy = candy + student['candies']
    return candy

print(get_all_candies_of_under_10(students))


# # write out the 2nd studtent's name
#
print(students[1]['name'])
#
#
# # write out all students' age
#
for student in students:
    print(student['age'])
#
# # write out student names who are younger than 10
#
for student in students:
    if student['age'] < 10:
        print(student['name'])
#
# # write out the total candy of all the students who are younger than 10
candy = 0

for student in students:
    if student['age'] < 10:
        candy = candy + student['candies']
print(candy)
