#Lists - a datatype that can hold multiple values.
#Lists are ordered, changeable, and allow duplicate values.
#Represented by square brackets [] and items are separated by commas.
students = ["Hermione", "Harry", "Ron"]
# print(students[1]) #accessing the second element of the list (index starts at 0)

# for student in students: #iterating through the list
#     print(student)

for i in range(len(students)): #iterating through the list using index
    print(i+1, students[i])


#len - a built-in function that returns the number of items in a list.
