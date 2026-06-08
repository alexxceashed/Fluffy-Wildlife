# Transit Photometry Tools

This folder contains several Python tools for working with TESS FITS data, extracting transit candidates, parsing FITS headers, plotting light curves, and estimating exoplanet properties.

## Contents

- `variable_finder.py` — main transit search pipeline that reads a FITS file, flattens the light curve, runs a Box Least Squares search, and computes a candidate period, transit depth, orbital radius, and planet radius.
- `fits_parser.py` — opens a FITS file, prints a summary of the HDU structure, and lists header keywords.
- `fits_retriever.py` — downloads a FITS file from a user-provided URL.
- `image_data_parser.py` — reads a FITS light curve and plots the raw flux vs time.
- `exoplanet_profiler.py` — helper script with orbital radius and planet radius functions for manual input.
- `FITS Files/` — a directory that can store FITS files used by the tools.

## Requirements

These scripts use the following Python packages:

- `astropy`
- `numpy`
- `scipy`
- `matplotlib` (for `image_data_parser.py`)
- `wotan` (for `variable_finder.py`)

Install them with pip if needed:

```bash
python -m pip install astropy numpy scipy matplotlib wotan
```

## How the files work

### `variable_finder.py`

This is the main analysis script.

1. Prompts for a FITS file name and locates the file in the script directory.
2. Reads the primary FITS header and extracts stellar parameters:
   - `TEFF` (effective temperature)
   - `RADIUS`
   - `LOGG` (surface gravity)
3. Computes stellar luminosity, mass, and surface gravity using simple scaling relations.
4. Loads the light curve from the second HDU (`[1].data`) and selects a flux column in this order:
   - `PDCSAP_FLUX`
   - `LC_INIT`
   - `SAP_FLUX`
   - fallback to the first column containing `FLUX`
5. Cleans the data by removing NaN values and non-positive flux values.
6. Flattens the light curve using `wotan.flatten`.
7. Runs `astropy.timeseries.BoxLeastSquares` over a period range of 2.5 to 4.0 days and a set of durations.
8. Uses `scipy.signal.find_peaks` to identify the top BLS power peaks.
9. Prints the top period candidates and selects the strongest peak.
10. Calculates orbital radius and planet radius using `exoplanet_profiler.orbital_radius` and `planet_radius`.

**Important notes:**

- The script assumes the FITS file contains a TESS light curve in a standard format.
- It is designed for targets where a ~2.5–4 day period transit signal is expected.
- The `planet_radius()` formula assumes the depth represents a fractional transit depth and that the stellar radius is in units of solar radii.
- If the result is an impossible radius, double-check the selected depth, the input FITS file type, and whether the file contains a properly processed light curve.

### `fits_parser.py`

This utility:

1. Prompts the user for a FITS file name.
2. Locates the file in the script directory.
3. Opens the FITS file with `astropy.io.fits`.
4. Prints the file structure with `hdul.info()`.
5. Prints all header keywords from the primary HDU.

Use this file to inspect FITS contents and verify that the expected metadata is present.

### `fits_retriever.py`

This simple downloader:

1. Prompts for a URL.
2. Prompts for a numeric identifier.
3. Downloads the file from the URL using `urllib.request.urlretrieve`.
4. Saves it locally as `sample<num>.fits`.

This is useful for grabbing FITS files from an external source when you have a direct URL.

### `image_data_parser.py`

This script:

1. Prompts for a filename.
2. Loads the FITS file using `astropy.io.fits`.
3. Reads time and flux columns.
4. Plots the raw light curve with `matplotlib`.

**Note:** the current code contains a hard-coded `path` variable and will not use the entered file name correctly unless fixed. The intended behavior is to plot the selected FITS file's light curve.

### `exoplanet_profiler.py`

This helper module includes:

- `orbital_radius(tp, sm)` — estimates orbital radius using a simplified Kepler-style relation with period in days and stellar mass in solar masses.
- `planet_radius(r, td)` — estimates planet radius from stellar radius and transit depth using a scaling factor.

It also includes a CLI `main()` that asks for manual input and prints results.

## Recommended workflow

1. Use `fits_parser.py` first to inspect the FITS file structure and confirm the light curve columns.
2. Use `image_data_parser.py` to plot the raw light curve and identify whether the data are valid.
3. Use `variable_finder.py` to run the transit search and compute candidate properties.
4. If needed, use `exoplanet_profiler.py` to manually verify your radius calculations with known values.

## Troubleshooting

- If `variable_finder.py` returns an unrealistic planet radius, verify that:
  - the FITS file contains a real light curve (`PDCSAP_FLUX` is preferred)
  - the transit depth is a fractional value, not a percentage
  - the star radius is in solar radius units
- If the script fails to locate a file, ensure the file is in the same directory or a subdirectory under `Tools`.
- If `wotan.flatten` is not installed, run:

```bash
python -m pip install wotan
```

## File locations

- Put target FITS files in `Tools/` or a subdirectory under `Tools`.
- `fits_retriever.py` can download FITS files directly into the `Tools/` folder.

---

This README is intended as a reference for the Transit Photometry tools in this directory. Use it as a starting point when loading, validating, and analyzing TESS FITS data.
