def hello(name):
    print(f"Hello, {name}")
def goodbye(name):
    print(f"Hello, {name}")
def main():
    hello("David")
    goodbye("David")
if '__name__' == "__main__": #This condition checks if the script is being run directly (as the main program) rather than 
                             #imported as a module.
    main()