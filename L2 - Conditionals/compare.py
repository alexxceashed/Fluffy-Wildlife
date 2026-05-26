x = int(input("What's x?"))
y = int(input("What's y?"))

#Checking if x is greater than or lesser than y
if x < y:
    print("Y is greater than X")
elif y > x:
    print("X is greater than Y")
else: 
    print("X and Y are equal")


#if: The starting point. It checks a condition; if true, it runs the code block.
#elif (short for "else if"): Checks another condition only if the previous if or elif conditions were False.
#else: The final "catch-all". It runs only if all previous conditions were False
#or - if one condition is true, the whole block is true and statement is executed

#Checking if y == x or not
a = int(input("What's a?"))
b = int(input("What's b?"))
if a > b or a < b:
    print("A is not equal to B")
else:
    print("A is equal to B")
    

