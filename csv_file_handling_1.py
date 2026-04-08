# Reading CSV

import csv

with open('/var/www/html/python-projects/test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)