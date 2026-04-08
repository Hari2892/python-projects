# Writing CSV

import csv

data = [
    ['Name', 'Age'],
    ['Hari', 34],
    ['Bob', 30]
]

with open('/var/www/html/python-projects/test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)