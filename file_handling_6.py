


with open("/var/www/html/python-projects/test.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("/var/www/html/python-projects/test.txt") as f:
  print(f.read())