
students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

# create a function that counts the students that
# has more than 4 candies

def get_students_with_more_than_4_candies(input):
    total_students = 0
    for x in input:
        if x['candies'] > 4:
            total_students = total_students + 1
    return total_students

print(get_students_with_more_than_4_candies(students))
