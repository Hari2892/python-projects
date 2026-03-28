import json

# some JSON:
x = '{ "firstname":"Hariharan", "lastname":"R", "age":30, "city":"Sivaganga"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary: 
print(y["firstname"])
