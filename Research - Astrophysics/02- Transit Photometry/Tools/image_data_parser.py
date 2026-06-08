from astropy.io import fits as f
import matplotlib.pyplot as plt

filename = input("Enter Filename:")
path = r'C:\Users\Alex\Desktop\Fluffy-Wildlife\Research - Astrophysics\02- Transit Photometry\Tools\{works2.fits}'
print("Extracting telemry data from FITS file...")
with f.open(path) as hdul:
    tce_data = hdul[1].data #creates a dictionary of the data from the second HDU (index 1) of the FITS file, which contains the telemetry data for the TESS observation.
    time = tce_data['TIME'] # Extracts the time data from the telemetry data dictionary.\\
    available_columns = tce_data.names
    if 'PDCSAP_FLUX' in available_columns:
        flux = tce_data['PDCSAP_FLUX']
        print("-> Automatically loaded pipeline column: PDCSAP_FLUX")
    elif 'LC_INIT' in available_columns:
        flux = tce_data['LC_INIT']
        print("-> Automatically loaded custom column: LC_INIT")
    elif 'SAP_FLUX' in available_columns:
        flux = tce_data['SAP_FLUX']
        print("-> Automatically loaded raw column: SAP_FLUX")
    else:
    # Failsafe: find ANY column that contains the word 'FLUX'
        flux_col = [col for col in available_columns if 'FLUX' in col][0]
        flux = tce_data[flux_col]
        print(f"-> Failsafe matched column: {flux_col}") # Extracts the flux data from the telemetry data dictionary, which represents the light curve measurements of the observed star.
    print("Data extraction complete. Time and flux arrays created.")

plt.style.use('dark_background')
plt.plot(time,flux, color = 'white', marker = ".", ms = 2)
plt.title('TESS Light Curve: TIC 1001000827')
plt.xlabel('Time (Days)')
plt.ylabel('Relative Flux ')
plt.show()
