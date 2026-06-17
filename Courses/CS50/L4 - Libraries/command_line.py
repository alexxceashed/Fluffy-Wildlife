#sys - used for command-line arguments and other system-related functions.
import sys as s

#sys.argv - a list of command-line arguments passed to a Python script. 
#The first element is the script name, and the subsequent elements are the additional arguments.
# try: 
#     print(f"Hello, {s.argv[1]}!")
# except IndexError:
#     print("Too few arguments")

#check for errors
if len(s.argv) < 2:
    s.exit("Too few args")

for arg in s.argv[1:]:
    print (f"Hello, my name is {arg}")
#Greet user
'''print(f"Hello {s.argv[1]}!")'''

#0 index is the name of the program, 1 index is the first argument, and so on.
#passing arguements as you run the program leads to efficiency, as you don't have to hardcode values into your program.
#To run this program, you would use the command line and type something like:
#python command_line.py Alice Bob
#This would output:
#Hello, my name is Alice
#Hello, my name is Bob
#If you run the program without any arguments, it will output:
#Too few args
#This is a simple example of how to use command-line arguments in Python to greet users by their names.