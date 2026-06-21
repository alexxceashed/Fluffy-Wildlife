from datetime import date as d
import sys
import inflect
import re
p = inflect.engine()

def main():
    bday = birthday()
    print(f"{old(bday)}")

def birthday():
    try:
        return d.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

def old(date):
     tday = d.today()
     return f"{p.number_to_words(round((tday-date).days*1440), andword="").capitalize()} minutes"

if __name__ == "__main__":
    main()
