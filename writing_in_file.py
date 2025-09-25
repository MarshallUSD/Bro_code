# python writing files (.txt, .json, .csv)
#Working with txt file
"""""
employees=['jimmy','john', 'johnny']


file_path="C://Users//user//OneDrive//Desktop//out.txt"

try:
 with open(file_path, "a") as file:
     for a in employees:
          file.write(a+"\n")
     print(f"txt file in {file_path}")
except FileExistsError:
    print(f"txt file already exists")

# JSON file to write methods

import json

employee={
    'name': 'jimmy',
     'age': 22,
    'gender': 'male',
}

file_path="C://Users//user//OneDrive//Desktop//out.json"

try:
    with open(file_path, "w") as f:
        json.dump(employee, f, indent=4)
        print(f"json file in {file_path}")
except FileExistsError:
    print(f"json file already exists")
"""
# Writing to the CSV file
import csv

file_path="C://Users//user//OneDrive//Desktop//out.csv"
employees=[['name','age','job'],['Sponge',41,'cook'],['Patrick', 47, 'Unemployed'],['Sandy', 47, 'Scientist']]



try:
    with open(file_path, 'w', newline="") as f:

          writer = csv.writer(f)
          for row in employees:
              writer.writerow(row)
          print(f"csv file in {file_path}")
except FileExistsError:
    print(f"csv file already exists")

"""

# Python reading files


#Reading the .txt file

import json
try:
  with open(file_path, "r") as file:
    content = file.read()
    print(content)
except PermissionError:
    print(f"Permission error")
# Read in json file
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["gender"])
except FileNotFoundError:
    print(f"File not found")
"""

import  csv

file_path="C://Users//user//OneDrive//Desktop//out.json"

try:
    with open(file_path, "r", newline="") as file:

        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"File not found")
