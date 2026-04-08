# Writing CSV with Dictionary

import csv

data = [
    {'Name': 'Hariharan', 'Age': 34},
    {'Name': 'Bob', 'Age': 30}
]

with open('/var/www/html/python-projects/test.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)