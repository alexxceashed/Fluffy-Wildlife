# Astrophysical Modeling Commit Message Guide

This file documents suggested git commit messages for the `03 - Astrophysical Modeling` folder, organized by file and broad folder context.

## File-level commit messages

- `Tools/cleanup.py`
  - `script to remove NaN values from raw dataset and clean light curve data`

- `Tools/celestial_body.py`
  - `define CelestialBody model with validated mass/radius and Newtonian motion update`

- `Tools/gravity.py`
  - `simulate gravitational attraction between two bodies with daily position updates`

- `Tools/redshift.py`
  - `convert redshift into cosmological distances and universe age using Astropy`

- `Tools/SAMBAD.py`
  - `query SIMBAD for star magnitude, parallax, and distance`

- `Tools/README.md`
  - `document Tools folder usage, dependencies, and AI-assisted learning notes`

- `README.md` in `03- Astrophysical Modeling`
  - `add concise parent README for Astrophysical Modeling workspace`

## Folder-level commit messages

- `Research - Astrophysics/03- Astrophysical Modeling/Tools/`
  - `add interactive astrophysics utilities for data cleaning, simulation, cosmology, and catalog lookup`

- `Research - Astrophysics/03- Astrophysical Modeling/Objects/`
  - `add reusable celestial object model support for physics simulations`

- `Research - Astrophysics/03- Astrophysical Modeling/`
  - `set up Week 3 astrophysical modeling workspace with overview documentation`

## Usage note

These messages are intended to be used when committing the relevant file or folder changes, keeping the commit description aligned with the code's behavior and purpose.