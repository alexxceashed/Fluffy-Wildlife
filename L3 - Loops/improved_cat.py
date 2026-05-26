def main():
    d_num = get_number()
    meow(d_num)
def get_number():
    n = int(input("Enter desired value:"))
    while n < 0:
        n = int(input("Enter a non-negative value:"))
    return n
def meow(iterations):
    for _ in range(iterations):
        print("Meow")
main()

    
