
#Dictionaries - a datatype that can hold multiple values in key-value pairs.
#Dictionaries are unordered, changeable, and do not allow duplicate keys.
#Represented by curly braces {} and key-value pairs are separated by commas.
students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}
print(students["Hermione"]) #accessing the value associated with the key "Hermione"
print(students["Draco"]) #accessing the value associated with the key "Draco"

for student in students: #iterating through the dictionary keys
    print(student, students[student], sep = " - ") #printing the key and its associated value
