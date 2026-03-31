with open("/var/www/html/python-projects/test.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("/var/www/html/python-projects/test.txt") as f:
  print(f.read())