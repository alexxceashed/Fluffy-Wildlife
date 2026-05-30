Welcome to the **Week 1 Astrophysics Portfolio**. This folder contains a suite of Python-based simulations and data visualization tools that bridge the gap between computational logic (CS50 concepts) and real-world astrophysics.

## 📂 Folder Contents

### 1. `mission_control.py` (Orbital Dynamics Engine)
* **Objective:** Calculates critical orbital thresholds (Circular and Escape Velocity) for spacecraft.
* **Key Features:** * Handles unit conversions from Observational (AU, Solar Masses) to SI (Meters, Kilograms).
  * Robust user input sanitization (`try/except` blocks).
  * Decision tree logic to determine orbit stability based on probe velocity.

### 2. `solar_system_plot.py` (Keplerian Data Visualization)
* **Objective:** Visually proves **Kepler's Third Law** ($P^2 \propto a^3$).
* **Key Features:**
  * Plots the Semi-Major Axis vs. Orbital Period of the 8 planets.
  * Utilizes **Log-Log scaling** in Matplotlib to transform the power-law curve into a linear proof of universal gravitation.

### 3. `luminosity.py` (Stellar Power Law)
* **Objective:** Demonstrates the **Mass-Luminosity Relationship** for main sequence stars ($L \approx M^{3.5}$).
* **Key Features:**
  * Math operations across arrays to generate theoretical data sets.
  * Logarithmic plotting spanning over seven orders of magnitude, anchored perfectly at the Sun (1.0 $M_{\odot}$, 1.0 $L_{\odot}$).

### 4. `hertzprung-russell.py` (Hertzsprung-Russell Stellar Classification)
* **Objective:** Plots a professional-grade H-R diagram (Temperature vs. Luminosity) to classify stars into their evolutionary stages.
* **Key Features:**
  * Dynamically collects and plots user data.
  * Conditionally colors stars based on their surface temperature (Spectral Class).
  * Features an inverted X-axis and logarithmic Y-axis to match astronomical standards.
  * Includes a baseline Main Sequence reference line to easily identify Giants, Supergiants, and White Dwarfs.

## 🛠️ Technologies & Skills
* **Language:** Python 3
* **Libraries:** `matplotlib.pyplot`, `numpy` (if used)
* **Concepts Applied:** Loops, Lists, String Parsing, Data Structures, Error Handling, Vectorized Math, Scientific Data Visualization.

---
*Built as part of an intensive computational astrophysics sprint.*