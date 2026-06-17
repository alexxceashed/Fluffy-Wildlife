
    
#while loops- used for executing a block of code repeatedly as long as a given condition is true. 
#The condition is evaluated before executing the block of code. 
#If the condition is false, the loop will not execute at all.

'''In this example, the loop will execute as long as the value of i is not equal to 0.'''
# i = 3
# while i != 0:
#     print("Meow")
#     i -= 1


#List - a datatype that can hold multiple values.
#Lists are ordered, changeable, and allow duplicate values.
#Represented by square brackets [] and items are separated by commas.
# for _ in range(10):
#     print("Meow")


'''asking the user how many times he wants to meow'''
n = int(input("How many times do you want to meow? "))
while n < 0:
    n = int(input("Please enter a positive number."))
    if n >= 0:
        break
    elif n < 0:
        continue

#for loops- used for iterating over a sequence (like a list, tuple, string) 
# or other iterable objects.
for _ in range(n):
    print("Meow")