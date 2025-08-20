import csv

# with open('temp.csv', 'w') as file:
#     fieldName = ['name', 'age', 'gender']
#     csv_writer = csv.DictWriter(file, fieldnames=fieldName)
#     csv_writer.writeheader()

with open('temp.csv', 'r') as file:
    field = ['name','age','gender']
    csv_reader = csv.DictReader(file, fieldnames=field)
    for line in csv_reader:
        if(line['name']=="bot"):
            print(line['gender'])

# with open('temp.csv', 'a') as file:
#     field = ['name', 'age', 'gender']
#     csv_writer = csv.DictWriter(file, fieldnames=field)
#     li = {
#         'name':'bot',
#         'age':19,
#         'gender':'nb'
#     }
#     csv_writer.writerow(li)


with open('temp.csv', 'a') as file:
    field = ['name', 'age', 'gender']
    csv_writer = csv.DictWriter(file, fieldnames=field)
    csv_writer.writerow({'name':'bot', 'age' : 19, 'gender' : 'male'})