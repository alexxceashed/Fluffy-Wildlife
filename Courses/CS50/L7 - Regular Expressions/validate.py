#Regular Expressions -  Used to find patterns in text.  
# Can be used to validate input, search for patterns, and more.
import re

#Program to compare input with a sample email address to validate it.
email = input("Enter Email: ").strip()
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")
#        OR

# username, domain = email.split("@")
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

#The code could further be iterated to check for more specific patterns in the email address, 
# such as ensuring that the username and domain contain only valid characters, 
# and that the domain has a valid top-level domain (TLD).
# But this will be too complex and not very efficient. Instead, we can use regular expressions to validate the
#  email address more effectively.

if re.search(r"^[\w._]+@(\w+\.)?\w+\.(com|edu|net|org|co|gov|)$", email, re.IGNORECASE): #flags are configuration options that can be passed to the re.search() function to modify its behavior.
    #re.dotall - This flag allows the dot (.) in the pattern to match newline characters as well, enabling it to match across multiple lines.
    #re.multiline - This flag allows the pattern to match across multiple lines, treating each line as a separate string.
    #re.ignorecase - This flag makes the pattern matching case-insensitive, meaning it will match letters regardless of whether they are uppercase or lowercase.
    print("Valid")
else:
    print("Invalid")

#Regex symbols
#. - Matches any character except a newline.
#+ - Matches one or more of the preceding character or group.
#* - Matches zero or more of the preceding character or group.
#$ - Matches the end of the string.
#^ - Matches the start of the string.
#{n} - Matches exactly n occurrences of the preceding character or group.

#[] - set of characters
#[^] - negated set of characters meaning it can be anything except the characters in the set.
#? - Matches zero or one of the preceding character or group, making it optional.

#\w - Matches any alphanumeric character (letters and digits) and underscore (_).
#\d - Matches any digit (0-9).
#\s - Matches any whitespace character (spaces, tabs, newlines).
#\W - Matches any non-alphanumeric character (anything that is not a letter, digit, or underscore).
#s - Whitespace character
#S - Non-whitespace character
#\D - Matches any non-digit character (anything that is not a digit).
