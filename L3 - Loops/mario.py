def main():
    print_square(3)

def print_column(b): #prints # for a tower for b times.
    for _ in range(b):
        print("#")
def print_row(c):
    for _ in range(c):
        print("?", end = "")
def print_square(a):
    for i in range (a):
        for j in range(a):
            print("#", end = "")
        print()

main()