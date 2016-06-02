import csv
#
# g = open('names.csv', 'w')
# fieldnames = ['first_name', 'last_name']
# text = csv.writer(g, fieldnames=fieldnames)
# writer.writerow('Bucky', 'Telo')
#
with open('names.csv', 'w') as csvfile:
    fieldnames = ['Status', 'Task']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Status': 'True', 'Task': 'Walk the dog'})
