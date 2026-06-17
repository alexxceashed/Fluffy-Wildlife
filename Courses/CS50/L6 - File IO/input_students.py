import csv
name = input("Enter name: ")
home = input("Enter home: ")

with open("students2.csv", "a", newline = "") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"]) #This creates a DictWriter object that will write dictionaries to the CSV file. 
    #The fieldnames parameter specifies the order of the columns in the CSV file.
    writer.writerow({"name": name, "home": home})
    #The writerow() method is called to write a single row to the CSV file. The row is represented as a dictionary, where the keys correspond to the field names specified earlier.

