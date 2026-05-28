def main():
    x = get_int("What's x?")
    print(f"x is {x}")


def get_int(p):
    while True:
        try:
            return int(input(p))
        except ValueError:
            pass
main()

#try-except block is used to handle exceptions that may occur during the execution of a program. 
# In this code, the get_int function prompts the user for input and attempts to convert it to an integer. 
# If the user enters a value that cannot be converted to an integer (e.g., a string), a ValueError will be raised. 
# The except block catches this exception and allows the program to continue running without crashing, prompting the user again until a valid integer is entered.

#raise- The raise statement is used to manually trigger an exception in Python.
# It allows you to specify the type of exception you want to raise and an optional error message.
# For example, you can use raise to signal an error condition in your code or to indicate 
# that a certain condition has not been met. 
# When the raise statement is executed, it interrupts the normal flow of the program and 
# transfers control to the nearest exception handler that can handle the specified exception type.