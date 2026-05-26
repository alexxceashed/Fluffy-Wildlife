name = input("What is the name ")
# if name == "Harry" or name == "Hermione" or name == "Ron": 
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

#ORRRR
match name:
    case "Harry" | "Hermione" | "Ron": #tighter syntax, more concise, easier to read
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")