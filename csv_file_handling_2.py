# Reading CSV as Dictionary

import csv

with open('/var/www/html/python-projects/test.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'])