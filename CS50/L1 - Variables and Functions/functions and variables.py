#string - datatype used to yield characters, phrases etc.
#ask user for their name
name = input("What's your name? ")

#Remove whitespace from string and capitalize the first letter of each word (Chaining)
name = name.strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

#replace something in the string
first = first.replace("Digvijay", "Alex")

#say hello to user
print(f"Hello, {first}")


#fstring - special type of string that allows you to embed variables and expressions directly inside a string. 
#print(*objects (meaning the function can have any type of input), sep = ' ' (inserts space when using comma for inserting multiple values of datatypes), end ='\n'(ends the print function with a new line always.))


#parameters - placeholder variable in a function's definition
#arguments - actual value passed to the function when called 
#functions - actions that lets us do something in the program. every programming language comes with a basic set of functions that the computer already knows.

