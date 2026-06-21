import re 
name = input("Enter name: ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
    name = f"{matches.groups(1)} {matches.groups(2)}"
print(f"Hello, {name}")
