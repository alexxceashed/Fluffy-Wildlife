students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None} #list of dictionaries that contains information about students
    #how exactly does this work - it is a list of dictionaries, where each dictionary represents a student and 
    # contains key-value pairs for the student's name, house, and patronus. 
    # The list allows us to store multiple students, and the dictionaries allow us to 
    # store multiple pieces of information about each student in an organized way.

            ]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = " - ") #iterating through the list of dictionaries 
#and printing the name, house, and patronus of each student