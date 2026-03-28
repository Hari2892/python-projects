import json

x = {
  "firstname": "Hariharan",
  "lastname": "R",
  "age": 30,
  "married": True,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values: 
print(json.dumps(x, indent=4, separators=(". ", " = ")))
