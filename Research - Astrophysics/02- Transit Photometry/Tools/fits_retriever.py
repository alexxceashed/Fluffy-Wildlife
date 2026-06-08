import urllib.request

# NASA MAST Archive URL for a TESS Data Validation File
url = input("Enter URL: ")
num = int(input("Enter number: "))
filename = f"sample{num}.fits"

print("Downloading payload from NASA MAST Archive...")
urllib.request.urlretrieve(url, filename)
print(f"Success! {filename} secured in your directory.")