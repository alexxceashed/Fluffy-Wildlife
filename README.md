# 🌌 Astrophysics & Computer Science Portfolio

Welcome to my central repository! This workspace tracks my journey through computer science fundamentals and applied computational astrophysics. It serves as a living portfolio of my coursework, programming experiments, and scientific simulations.

The repository is divided into two main branches: **Courses** (foundational learning) and **Astrophysics Research** (applied physics and data programming).

---

## 📂 1. Courses

This directory contains code written while studying computer science and data visualization. 

### `cs50/` (CS50: Introduction to Computer Science)
This folder contains my progress through Harvard's CS50 curriculum. 
* **Contents:** Lecture follow-alongs, experimental scripts, and self-produced practice code exploring data structures, memory management, algorithms, and Python logic.
* **Note on Academic Honesty:** In strict adherence to CS50's academic honesty policy, **this folder does not contain any solutions to graded Problem Sets (Psets).** It is purely a sandbox for lecture concepts and personal experimentation.

### `matplotlib/` (Data Visualization)
This folder tracks my mastery of the `matplotlib` library in Python, which is the backbone of my astrophysics research.
* **Contents:** Lecture codes, syntax practice, and self-produced experimental graphs.
* **Skills Covered:** Logarithmic scaling, scatter plots, array manipulation, custom color-mapping, and scientific plot formatting.

---

## 🚀 2. Astrophysics Research

This directory is where computer science meets the cosmos. The current module, **`01 - Orbital Mechanics`**, is structured functionally into four dedicated sub-directories to maintain a professional, scalable research environment:

### `derivations/` (Theoretical Foundations)
The math happens here before it ever touches the code. 
* **Purpose:** Contains the mathematical proofs, conceptual derivations, and theoretical groundwork for the physics engines.
* **Contents:** Documentation and notes explaining the equations behind orbital velocity limits ($v = \sqrt{GM/r}$), Kepler's Third Law ($P^2 \propto a^3$), and Stellar Power Laws ($L \approx M^{3.5}$).

### `simulations/` (Visual Astrophysics)
This folder houses the primary programs that visually model astrophysical phenomena, turning pure math into scientific charts and decision trees.
* **Contents:** * `hertzprung-russell.py`: A dynamic H-R diagram generator mapping Stellar Temperature vs. Luminosity to categorize stars into their evolutionary stages.
  * `luminosity.py`: Demonstrates the exponential mass-luminosity relationship across multiple orders of magnitude.
  * `mission_control.py`: The main Gravity and Orbital Dynamics Engine. It calculates circular/escape velocities and simulates probe trajectories (Crash, Orbit, or Escape).
  * `solar_system_plot.py`: Visually proves Kepler's Third Law using log-log plots.

### `tools/` (Utility Scripts & Calculators)
The backend logic and computational calculators that process specific parameters.
* **Contents:** * `escape_velocity_calculator.py`: A dedicated script to compute the exact velocity required to escape a celestial body's gravitational well.
  * `orbital_period.py`: Calculates the theoretical orbital periods of planets and satellites based on orbital distance and host mass.

### `validation/` (Quality Assurance & Output Proofs)
Where the code is tested and proven against reality. 
* **Purpose:** This folder contains the **proof of code in detail**. It acts as the visual and mathematical validation that all scripts in the simulations and tools folders execute correctly.
* **Contents:** Verified graphical outputs confirming script accuracy:
  * `hertzprung_russell_diagram1.png` & `hertzprung_russell_diagram2.png`: Proof of accurate star classification, color mapping, and log scaling.
  * `kepler_plot.png` & `orbital periods.png`: Validation of Kepler's 3rd Law mechanics.
  * `mass vs luminosity.png`: Proof of the stellar power law generation.
  * `mission_control.png`: Console/terminal proof verifying the orbital decision tree logic.

---
*End of transmission. Portfolio architecture mapped and ready.*