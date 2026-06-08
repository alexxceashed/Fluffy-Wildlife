from astropy.io import fits as f
import math as m
from astropy.timeseries import BoxLeastSquares
import numpy as np
from exoplanet_profiler import orbital_radius, planet_radius
import sys 
import scipy
import os
from wotan import flatten


SIGMA = 5.67*(10**-8)
PI = m.pi
UNIVERSAL_GRAVITATION_CONSTANT = 6.67*(10**-11)

def main():
    files = filename() 
    STemp,SRadius,SLuminosity,SMass,SGravity = stellar_maths(files)
    ORadius,PRadius,OPeriod = transit_math(files, SMass, SRadius)
    print(f"\nTemperature: {STemp:.2f}K \nRadius: {SRadius:.2f}R. \nLuminosity: {SLuminosity:.2f}L. \nMass: {SMass:.2f} \nSurface Gravity: {SGravity:.2f} \nOrbital Period: {OPeriod:.4f}\nOrbital Radius: {ORadius:.2f}AU \nPlanet Radius: {PRadius:.4f}RJup")
def filename():
    print("\n🌟 Exoplanet Pipeline Initialized")
    raw_input = input("Enter the name of your data file (e.g., sample4.fits): ")
    clean_name = raw_input.strip(' "\'')
    
    if not clean_name.lower().endswith('.fits'):
        clean_name += '.fits'

    script_dir = os.path.dirname(os.path.abspath(__file__))
    for root, dirs, files in os.walk(script_dir):
        if clean_name in files:
            return os.path.join(root, clean_name)

    print(f"\n❌ File not found: {clean_name}")
    sys.exit()
def stellar_maths(file):
    hdul = f.open(file)
    head_info = hdul[0].header
    # 1. Safely extract the parameters (they will equal 'None' if missing)
    K = head_info.get('TEFF')
    G = head_info.get('LOGG')
    R = head_info.get('RADIUS')
    
    # 2. The Verification Gate (Fail Fast)
    if K is None or R is None:
        print("\n❌ FATAL ERROR: Invalid FITS file.")
        print("Critical stellar parameters (TEFF or RADIUS) are missing from the header.")
        print("Exiting program to prevent inaccurate calculations.")
        sys.exit() # This completely stops the script right here!
    if R > 2.0:
        print(f"⚠️  WARNING: R = {R:.2f} R☉ — possible giant/subgiant star.")
        print("   The mass-luminosity relation (M = L^(1/3.5)) assumes a")
        print("   main-sequence star. Mass estimate may be unreliable.")

    # 3. If the script survives the check above, it means the data is good!
    print(f"--- Star Data Verified ---")
    R_SI = R*(6.957*(10**8))
    # The Stefan-Boltzmann Law (Relative Form)
    # states the total energy radiated by a black body (like a star) is proportional to its surface area and the fourth power of its temperature. 
    # We use the relative form to compare it directly to our Sun.
    L = (R**2) * (K/5778)**4
    #Mass-Luminosity Relation
    M = L**(1/3.5)  
    M_SI = M * (1.989*(10**30))
    #Gravitational Law of Newton
    g = (UNIVERSAL_GRAVITATION_CONSTANT*M_SI)/(R_SI**2)
    g_CGS = g*100
    g_Surface = m.log10(g_CGS)
    return K,R,L,M,g_Surface
def transit_math(file, Mass, Radius):
    hdul = f.open(file)
    tce_data = hdul[1].data #creates a dictionary of the data from the second HDU (index 1) of the FITS file, which contains the telemetry data for the TESS observation.
    time = tce_data['TIME'] # Extracts the time data from the telemetry data dictionary.
    print("-> Automatically loaded pipeline column: TIME")
    available_columns = tce_data.names # Get a list of all column names in the file

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

    if 'LC_INIT' in available_columns and 'PDCSAP_FLUX' not in available_columns:
        print("⚠️  WARNING: This appears to be a DVT/validation file, not a standard light curve.")
        print("   Planet radius and period results will be unreliable.")
        print("   Download the _lc.fits file for this target instead.")

    clean_mask = ~np.isnan(flux) & ~np.isnan(time) & (flux > 0)
    clean_time = time[clean_mask]
    raw_flux = flux[clean_mask] / np.median(flux[clean_mask])

# Flatten the light curve baseline before transit search
    print("Flattening light curve baseline...")
    n_points = len(clean_time)
    timespan_days = clean_time[-1] - clean_time[0]
    cadence_days = timespan_days / n_points
    kernel = int(round(0.125 / cadence_days))  # ~3 hours of data
    if kernel % 2 == 0:
        kernel += 1  # medfilt requires an odd number
    kernel = max(kernel, 3)
    print(f"Flattening with kernel = {kernel} points")
    clean_flux, trend = flatten(clean_time, raw_flux, method='biweight', window_length=0.75, return_trend=True)   

    print("Running BoxLeastSquares Engine...")
    model = BoxLeastSquares(clean_time, clean_flux)
    durations = np.linspace(0.04, 0.25, 8)   # hours-to-days range, not fraction of period
    results = model.power(np.linspace(2.5, 4.0, 5000), durations, objective='snr')


# 4. Find the Top 3 Mathematical Candidates
    peaks, _ = scipy.signal.find_peaks(results.power, distance=50)
    sorted_peaks = sorted(peaks, key=lambda x: results.power[x], reverse=True)

    print("\n--- Pipeline Top 3 Period Candidates ---")
    for i in range(min(3, len(sorted_peaks))):
        idx = sorted_peaks[i]
        print(f"Candidate {i+1}: Period = {results.period[idx]:.4f} days | Depth = {results.depth[idx]:.5f}")

# 5. Select the strongest transit candidate by peak power
    if len(sorted_peaks) > 0:
        best_index = sorted_peaks[0]
    else:
        best_index = np.argmax(results.power)

    transit_period = results.period[best_index]
    raw_transit_depth = results.depth[best_index]
    depth_err = results.depth_err[best_index]
    depth_err = results.depth_err[best_index]
    
    if depth_err != 0:
        snr = raw_transit_depth / depth_err
        if depth_err != 0:
            snr = raw_transit_depth / depth_err
            print(f"Transit SNR: {snr:.3f}")
            if snr < 7.0:
                print("⚠️  WARNING: Low SNR — this may be noise, not a real transit.")
                print("   Treat the planet radius result with caution.")
    fractional_depth = raw_transit_depth
    
    # DEBUG: Print selected values before physics calculation
    print(f"\n--- Selected Best Transit ---")
    print(f"DEBUG: transit_period = {transit_period:.6f}")
    print(f"DEBUG: raw_transit_depth = {raw_transit_depth:.10f}")
    print(f"DEBUG: Radius input = {Radius:.6f}")

    orbit_radius = orbital_radius(transit_period, Mass)
    p_radius = planet_radius(Radius, fractional_depth)

    return orbit_radius,p_radius,transit_period
main()
#print(f"Effective Temperature: {temperature}K \nStellar Radius: {radius}S. \nLuminosity of Star: {L}L. \nMass of Star: {M}M. \nSurface Gravity: {g}")



