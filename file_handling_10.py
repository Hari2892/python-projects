import os

folder_path = "/var/www/html/python-projects/test_folder"

if os.path.isdir(folder_path):
    os.rmdir(folder_path)
    print("The folder deleted successfully!")
else:
    print("Folder does not exist.")