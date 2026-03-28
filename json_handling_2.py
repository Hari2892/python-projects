import json

# a Python object (dict):
x = {
  "firstname": "Hariharan",
  "lastname": "R",
  "age": 30,
  "city": "Sivaganga"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
