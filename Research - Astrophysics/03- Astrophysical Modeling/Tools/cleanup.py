"""cleanup.py

Simple interactive tool to load a light-curve table from a FITS file,
clean the flux data, and plot original vs cleaned light curves.

Intended behaviour:
- Ask user for a `.fits` filename located next to this script.
- Attempt to detect common time and flux column names.
- Remove NaNs and perform a basic 5-sigma clip to remove outliers.
- Plot both the raw and cleaned light curves for quick inspection.

This file is designed for interactive exploration, not batch pipelines.
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import os
import sys


def get():
    """Prompt for a .fits filename located in the script directory.

    Returns the absolute path to the file. Repeats prompt until a valid
    filename is supplied.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        file = input(".fits file: ").strip()
        # expect the file to be in the same folder as this script
        if file.endswith(".fits") and os.path.exists(os.path.join(script_dir, file)):
            return os.path.join(script_dir, file)
        print("File doesn't exist.")


def engine(f):
    """Load FITS table and return raw and cleaned time/flux arrays.

    Parameters
    - f: path to the FITS file

    Returns a tuple: (raw_time, raw_flux, clean_time, clean_flux)

    Cleaning steps:
    1. Detect time column from common names ("TIME", "BTJD", "BJD").
    2. Detect flux column from a prioritized list of candidates.
    3. Convert columns to numpy floats.
    4. Remove NaNs from the flux (and corresponding times).
    5. Apply a 5-sigma median clip to remove extreme outliers.
    """
    hdul = fits.open(f)
    # assume the first extension (1) contains the table
    data = hdul[1].data

    # --- detect time column -------------------------------------------------
    for col in ("TIME", "BTJD", "BJD"):
        if col in data.columns.names:
            raw_time = np.array(data[col], dtype=float)
            break
    else:
        print("[ERROR] No time column found.")
        sys.exit(1)

    # --- detect flux column (priority order) -------------------------------
    flux_candidates = ['LC_INIT', 'LC_WHITE', 'FLUX', 'SAP_FLUX', 'PDCSAP_FLUX']
    flux_col = None
    for col in flux_candidates:
        if col in data.columns.names:
            flux_col = col
            break
    if flux_col is None:
        print("[ERROR] No valid flux column found.")
        print(f"Available columns: {list(data.columns.names)}")
        sys.exit(1)

    raw_flux = np.array(data[flux_col], dtype=float)

    # --- Stage 1: Remove NaNs -----------------------------------------------
    # Build a mask for flux values that are not NaN, then apply to both arrays
    nan_mask = ~np.isnan(raw_flux)
    time_nonan = raw_time[nan_mask]
    flux_nonan = raw_flux[nan_mask]

    # --- Stage 2: 5-sigma clipping -----------------------------------------
    # Compute median and standard deviation and reject points beyond 5-sigma
    median = np.median(flux_nonan)
    std = np.std(flux_nonan)
    sigma_mask = (flux_nonan >= median - 5 * std) & (flux_nonan <= median + 5 * std)

    clean_time = time_nonan[sigma_mask]
    clean_flux = flux_nonan[sigma_mask]

    # Return the original raw arrays and the cleaned arrays
    return raw_time, raw_flux, clean_time, clean_flux


def plot(raw_time, raw_flux, clean_time, clean_flux):
    """Plot the original and cleaned light curves using scatter plots.

    The plots are simple and intended for fast visual inspection. Large
    datasets will be plotted with small marker size (`s=1`) to reduce
    overplotting.
    """
    plt.figure(1)
    plt.scatter(raw_time, raw_flux, s=1, color="steelblue")
    plt.title("Original Light Curve")
    plt.xlabel("Time (BTJD)")
    plt.ylabel("Flux (e⁻/s)")
    plt.tight_layout()

    plt.figure(2)
    plt.scatter(clean_time, clean_flux, s=1, color="mediumseagreen")
    plt.title("Cleaned Light Curve")
    plt.xlabel("Time (BTJD)")
    plt.ylabel("Flux (e⁻/s)")
    plt.tight_layout()

    plt.show()


def main():
    # Run the interactive workflow: prompt -> load & clean -> plot
    file = get()
    raw_time, raw_flux, clean_time, clean_flux = engine(file)
    plot(raw_time, raw_flux, clean_time, clean_flux)


if __name__ == "__main__":
    main()