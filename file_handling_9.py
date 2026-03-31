import os
if os.path.exists("/var/www/html/python-projects/test2.txt"):
  os.remove("/var/www/html/python-projects/test2.txt")
  print("The file deleted successfully!")
else:
  print("The file does not exist")