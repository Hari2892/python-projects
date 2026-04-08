# Reading JSON

import json

with open('/var/www/html/python-projects/test.json', 'r') as file:
    data = json.load(file)   # string → dict

    json_text = json.dumps(data)     # dict → string

print(data)