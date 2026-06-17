# with open("students.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",")

#         print(f"{name}: {house}")

import csv 

students = []
with open("students.csv") as file:
    reader = csv.DictReader(file) #Reads the file as a CSV file
    #DictReader infers from the first row of the CSV file that there are two columns, "name" and "home".
    #The DictReader function reads the CSV file and creates a dictionary for each row, 
    # where the keys are the column names (in this case, "name" and "home") and the 
    # values are the corresponding values from that row.
    
    for row in reader: #Iterates through each row in the CSV file, where each row is represented as a dictionary.
        students.append({"name": row["name"], "home": row["home"]})  
        
        #This line is appending a dictionary to the students list. The dictionary has two keys: "name" and "home". The values for these keys are taken from the current row of the CSV file, using the column names as keys to access the values.
        #To the students list, a dictionary for EACH student is being appended.


def get_name(student):
    return student["name"]  #Takes in the dictionary, and returns the value of the key "name".

for student in sorted(students, key=get_name):
    print(f"{student['name']} is from {student['home']}")