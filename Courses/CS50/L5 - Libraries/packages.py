#pypi.org - a repository of software for the Python programming language. 
# It allows developers to share and distribute their Python packages, making it easier for others to find and use them.

#cowsay - a Python package that generates ASCII art of a cow saying a message.
#pip - a package manager for Python that allows you to install and manage additional libraries and dependencies that are not included 
#in the standard library.
#To install a package using pip, you can use the command line and run pip install package_name.

import cowsay as cw
import sys as s
# if len(s.argv) == 2:
#     cw.cow(f"Hello, {s.argv[1]}!")
# if len(s.argv) > 2:
#     cw.cow(f"Hello, {s.argv[1]} {s.argv[2]}")
if len(s.argv) == 2:
    cw.trex(f"Hello, {s.argv[1]}!")
if len(s.argv) > 2:
    cw.trex(f"Hello, {s.argv[1]} {s.argv[2]}")

p
