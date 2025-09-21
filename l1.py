# python file detection

import os

file_path= "C:/Users/user/OneDrive/Desktop/pp"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists.")
    if os.path.isfile(file_path):
        print(f"This is file in txt format.")
    elif os.path.isdir(file_path):
        print(f"This is folder")
    else:
        print(f"The location '{file_path}' is not a file.")
else:
    print(f"The location '{file_path}' does not exist.")


#C:\Users\user\PycharmProjects\PythonProject\stuff