# writing JSON

import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "Chennai"
}

with open('/var/www/html/python-projects/test.json', 'w') as file:
    json.dump(data, file, indent=4)