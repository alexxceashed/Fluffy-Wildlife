import re
url = input("URL: ").strip()
if matches := re.search(r"^(?:https?://)?(?:www\.)?x\.com/([\w\d_]+)", url, re.IGNORECASE):
    # username =re.sub(r"^(https?://)?(www\.)?x\.com/", "", url)
    print(f"Username: {matches.group(1)}") 
else:
    print("Invalid URL")