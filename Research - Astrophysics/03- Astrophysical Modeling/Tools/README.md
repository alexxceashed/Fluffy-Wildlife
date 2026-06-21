# Week 3: Astrophysical Modeling Tools

Welcome to the **Week 3: Astrophysical Modeling** repository. This folder contains a collection of Python utility scripts and modules designed for interactive data processing, orbital mechanics simulation, cosmological calculation, and astronomical catalog lookups. 

These tools serve as a practical playground for learning how core programming principles intersect with real-world astrophysics data.

---

## 📦 Requirements & Installation

These tools leverage industry-standard scientific Python libraries (`numpy`, `matplotlib`, `astropy`, and `astroquery`). 

### Core Dependencies
* **NumPy:** Powers the vectorized multi-dimensional matrix operations.
* **Matplotlib:** Handles time-series data visualization and orbital plotting.
* **Astropy:** Decodes `.fits` file headers, manages binary tables, and handles cosmological distance mathematics.
* **Astroquery:** Establishes API connections to fetch live metadata from the SIMBAD astronomical database.

To configure your environment, run the following command in your terminal:

```bash
python -m pip install numpy matplotlib astropy astroquery
```

> ⚙️ **Environment Note:** A minimum of **Python 3.8+** is required due to the use of modern syntax operations (such as assignment expressions).

## 📂 Core Script Registry

### 🪐 1. Kinematics Module: `celestial_body.py`
This module defines the structural blueprint of a celestial object using the `CelestialBody` class.

- **Properties:** Tracks data attributes including `name`, `position` (3D NumPy array), `velocity` (3D NumPy array), `mass`, and `radius`.
- **Encapsulation:** Employs property setters to prevent impossible physical metrics (e.g., negative mass or radius).
- **Kinematics Engine:** The `update(force_vector, dt)` method uses vectorized NumPy operations to resolve multi-axis Newtonian motion equations simultaneously.
- **Input Gate:** The `get()` classmethod utilizes regular expressions to safely parse, validate, and convert interactive user terminal inputs into clean vector components.
Bash

```
python celestial_body.py
```

### 🛰️ 2. Orbital Simulator: `gravity.py`
An execution script that simulates gravitational interactions across an extended timeline.

- **Logic:** Prompts for two distinct objects using `CelestialBody.get()` (e.g., a Sun and a planet).
- **Physics Loop:** Calculates gravitational attraction from the star toward the planet.
- **Star Behavior:** This is a basic simulation where the star is held fixed in place and only the planet is updated each step.
- **Time Step Engine:** Advances the simulation loop across 365 daily increments (`dt = 1.0`), printing periodic telemetry tracking updates to the terminal every 30 days.
Bash

```
python gravity.py
```

### 🧹 3. Data Pipeline: `cleanup.py`
An automated data-cleaning utility designed to process raw time-series photometry.

- **Ingestion:** Prompts for a local FITS file and loads the binary data table from HDU Index 1.
- **Fallback Resolution:** Automatically cross-references a priority queue of known astronomical headers to dynamically locate the appropriate time and flux columns.
- **Stage 1 Mask:** Purges dead sensor pixels by constructing an inverted Boolean mask (`~np.isnan()`) to remove missing data rows uniformly.
- **Stage 2 Filter:** Implements a single-pass 5-Sigma Clipping threshold (Median ± 5σ) to wipe out extreme instrumental outliers and cosmic ray impacts.
- **Visualization:** Renders an interactive Matplotlib frame comparing the noisy raw data against the cleaned stellar light curve.
Bash

```
python cleanup.py
```

### 🌌 4. Cosmology Calculator: `redshift.py`
A mathematical engine used to translate cosmological redshift values into physical distances.

- **Backbone:** Built on top of Astropy’s `Planck18` cosmology parameters.
- **Metrics Computed:** Solves for lookback time, comoving distance, luminosity distance, and the exact age of the universe at the moment light was emitted.
- **Formatting:** Automatically normalizes values into standard light-year scaling for straightforward comparison.
Bash

```
python redshift.py
```

### 🔭 5. Catalog Ingestion Tool: `SAMBAD.py`
An active database querying tool connecting directly to the international SIMBAD repository.

- **Operation:** Resolves user-submitted star names or catalog target identifiers.
- **Data Extraction:** Automatically parses the return payload to extract the target's V-band magnitude and parallax coordinates.
- **Unit Conversion:** Converts raw parallax coordinates from milliarcseconds into parsecs and light-years to determine true distance.
Bash

```
python SAMBAD.py
```

## 🛠️ Recommended Week 3 Workflow
To get the most out of this week's workspace, follow this logical processing track:

1. **Test Classical Mechanics:** Launch `gravity.py` and supply real physical constants for the Sun and Earth to witness multi-dimensional orbital tracking work in step-by-step loops.
2. **Process Telescope Data:** Run `cleanup.py` and feed it the provided `works.fits` sample file to see the automated fallback gate, NaN mask, and Sigma-Clipping filters clean up raw satellite data.
3. **Explore Deep Space Cosmology:** Utilize `redshift.py` to bridge the gap between observed target redshifts and the structural history/age of the universe.
4. **Validate Live Stellar Data:** Connect to the web via `SAMBAD.py` to lookup actual background values for observable stars, providing an absolute reference dataset for your calculations.

## ⚠️ Important Usage Tips

- **File Paths:** Always place raw `.fits` data files (like `works.fits`) directly into the same working directory as your execution scripts to guarantee seamless lookup resolution.
- **Internet Connection:** `SAMBAD.py` requires an uninterrupted internet connection to contact Strasbourg's servers. If an API request times out, check your local connection parameters first.
- **AI Pair Programming Note:** These modules were developed with AI architectural assistance to maximize code readability and clarify astronomical formulas. If an unhandled `KeyError` or input crash occurs, document the traceback error message and loop back to your AI assistant for a rapid hotfix patch.
