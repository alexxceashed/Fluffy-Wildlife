# 03 - Astrophysical Modeling

This folder contains the Week 3 astrophysical modeling projects, organized into two main subfolders:

- `Objects/` — contains object definitions, physical models, and reusable classes for celestial bodies.
- `Tools/` — contains interactive utilities for FITS data cleaning, catalog lookup, cosmology calculations, and simulation workflows.

## Overview

This directory is focused on applied astrophysics and scientific computing. The scripts are intended for exploration, learning, and small-scale simulation, rather than production pipelines.

## How to use this folder

1. Review the `Tools/README.md` file for detailed instructions on the utilities in the `Tools/` subfolder.
2. Run scripts from the folder where they live, for example:
   - `python Tools/cleanup.py`
   - `python Tools/redshift.py`
   - `python Tools/SAMBAD.py`
3. Use the `Objects/` folder for models and classes that support the tools and simulations.

## Requirements

Install the common scientific dependencies used in this folder:

```bash
python -m pip install numpy matplotlib astropy astroquery
```

Minimum recommended Python version: **Python 3.8+**.

## Notes

- `Tools/README.md` contains the detailed descriptions for the utility scripts.
- `Objects/` contains supporting physics models and reusable code.
- Internet access is required for `Tools/SAMBAD.py`.
