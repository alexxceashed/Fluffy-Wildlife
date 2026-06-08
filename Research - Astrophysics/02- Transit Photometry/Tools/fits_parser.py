from astropy.io import fits as f
import sys,os
print("\n🌟 Exoplanet Pipeline Initialized")
raw_input = input("Enter the name of your data file (e.g., sample4.fits): ")
clean_name = raw_input.strip(' "\'')

if not clean_name.lower().endswith('.fits'):
    clean_name += '.fits'

script_dir = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(script_dir):
    if clean_name in files:
        full_path = os.path.join(root, clean_name)
        break
else:
    print(f"\n❌ File not found: {clean_name}")
    sys.exit()
hdul = f.open(full_path)
hdul.info() #Print summary of the FITS file structure (rows, columns, data types, etc.)
#Name - represents the name of the HDU (Header Data Unit)
#Type - indicates the type of data stored in the HDU (e.g., PrimaryHDU, ImageHDU, BinTableHDU, etc.). 
    #BinTableHDU is a type of HDU that contains tabular data in binary format, often used for storing large datasets efficiently.
#Cards - shows the number of header cards (metadata entries) in the HDU
#Dimensions - indicates the dimensions of the data array in the HDU 
    #(e.g., 1000x1000 for an image, or the number of rows and columns for a table)
#Format - specifies the data format of the HDU (e.g., [D,E,J,E,E..] for a binary table, where D=double, E=float, J=integer, etc.)


head = hdul[0].header  #Creates a dictionary of the header information from the primary HDU (index 0) of the FITS file.
print("Header keywords: ")
for key,value in head.items(): #Prints each keyword and its corresponding value from the header dictionary. 
    #This allows you to see all the metadata associated with the primary HDU of the FITS file.
    print(f"{key}: {value}")
