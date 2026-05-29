# Summer Astro-Code 2026: Universal Orbital Dynamics

An independent research project exploring computational astrophysics through planetary mechanics and defensive programming. Developed during Class 11 summer break as part of an intensive 5-week "Elite Trajectory" roadmap.

## 🚀 Overview
This repository contains a suite of Python-based astrophysical tools designed to simulate and analyze celestial mechanics. The primary focus of Week 1 was the implementation of **Universal Orbital Period** and **Escape Velocity** calculators.

## 🛠️ Key Features
- **Universal Scale:** Handles systems ranging from Earth satellites to stars orbiting Supermassive Black Holes (Sgr A*).
- **Dual-Unit Support:** Accepts inputs in both SI units (kg, m) and standard observational units (Solar Masses, AU).
- **Robustness:** Implemented using `try-except` blocks and `while` loops to handle user errors (strings, negative values, etc.) gracefully.
- **Physics Foundation:** All calculations are derived from Newton's Law of Universal Gravitation.

## 📐 The Physics: Kepler's 3rd Law Derivation
The script utilizes the Newtonian form of Kepler's Third Law. The derivation connects Centripetal Force ($F_c$) and Gravitational Force ($F_g$):

1. $F_g = \frac{GMm}{r^2}$
2. $F_c = \frac{mv^2}{r}$
3. $v = \frac{2\pi r}{P}$

By setting $F_g = F_c$, we derive:
$$P = 2\pi \sqrt{\frac{r^3}{GM}}$$

*(Note: Handwritten mathematical proof is available in the `Derivations/` folder.)*

## 🧪 Validation Data
The code has been cross-verified against real-world celestial data:

| Test Case | Star Mass ($M_{\odot}$) | Radius (AU) | Calculated Period | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Earth** | 1.0 | 1.0 | 365.25 Days | ✅ Passed |
| **Jupiter** | 1.0 | 5.20 | 11.86 Years | ✅ Passed |
| **Moon** | 5.97e24 kg* | 3.84e8 m* | 27.45 Days | ✅ Passed |
| **TRAPPIST-1e** | 0.09 | 0.029 | 6.1 Days | ✅ Passed |
| **S2 (Black Hole)** | 4.3m $M_{\odot}$ | 1000 AU | 15.37 Years | ✅ Passed |

## 💻 Tech Stack
- **Language:** Python 3.10+
- **Libraries:** `math`
- **Principles:** Object-Oriented Logic, Functional Decomposition, Defensive Programming.

## 📂 Project Structure
- `/Calculators`: Core Python scripts (`universal_orbit.py`, `escape_velocity.py`).
- `/Derivations`: Scanned physics proofs and mathematical notes.
- `/Validation`: Spreadsheets of test cases and expected results.

---
**Author:** [Your Name/GitHub Username]
**Date:** May 2026
**Course:** CS50P (Introduction to Programming with Python) & Independent Astro-Study