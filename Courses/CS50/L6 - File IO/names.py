#File IO CS50 - Lecture 7
#variables like list, dictionary, set, tuple, string are all data structures that are stored
#in RAM (Random Access Memory) which is volatile memory. 
# When the program ends, all data stored in RAM is lost.
#Files are stored in non-volatile memory, such as a hard drive or SSD, and can be accessed even after the program ends.
#Files can be used to store data persistently, allowing you to read and write data across
#multiple runs of a program.
'''names = []
for _ in range(3):
    names.append(input("What's your name?: "))

for name in sorted(names):
    print(f"Hello, {name}")
Code stores names in memory, is lost immediately as program stops.
'''

#WRITING A FILE 
# name = input("What's your name? ")
#  #\n is a newline character, it moves the cursor to the next line after writing the name
# #with - automatically closes the file after the block of code is executed, even if an error occurs.
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


#READING EXISTING FILE
names = []
with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")
