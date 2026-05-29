def main():
    x = int(input("Enter number"))
    even_or_odd = eo(x)
    print(even_or_odd)

def eo(num):
    con = ""
    # if num % 2==0:
    #     con = "Even" #can also return boolean value, but only if we are checking if its ONLY even. for a single case, a true/false value works fine.
    # else:
    #     con = "Odd"
    return "Even" if num % 2 == 0 else "Odd"
main()