# Week 1: Foundational Mechanics & Defensive Scripting

This repository tracks the first phase of an intensive 5-week Computational Astrophysics roadmap. Week 1 focuses on moving from basic Python syntax to building robust, physically accurate models of orbital dynamics.

## 🎯 Week 1 "Elite 10" Gauntlet
| Status | Task | Category | Description |
| :--- | :--- | :--- | :--- |
| ✅ | **CS50P Core** | Logic | Completed Lectures 0-2 (Variables, Functions, Conditionals). |
| ✅ | **Newtonian Derivation** | Theory | Hand-derived Kepler’s 3rd Law from $F_g = F_c$. |
| ✅ | **Universal Orbit Script** | Coding | Developed `universal_orbit.py` with AU/Solar Mass support. |
| ✅ | **Crash-Proof Logic** | Robustness | Implemented `try-except` blocks for all user inputs. |
| ✅ | **Escape Velocity** | Physics | Built a secondary module for $v_e$ calculations across 3 regimes. |
| 🚧 | **Mission Control** | Logic | `if/elif/else` decision tree for probe deployment. |
| 🚧 | **Solar System Plot** | Viz | Matplotlib implementation of $a^3$ vs $T^2$. |
| 🚧 | **H-R Diagram Intro** | Viz | Initial Temperature vs. Luminosity scatter plotting. |
| 🚧 | **Mass-Luminosity** | Modeling | Scripting the $L \approx M^{3.5}$ relationship. |
| ✅ | **Portfolio Architecture**| DevOps | Established a professional research-grade folder structure. |

---

## 📐 Mathematical Foundations
The primary engine of this week's work is the **Newtonian Generalization of Kepler's Third Law**:

$$P = 2\pi \sqrt{\frac{a^3}{G(M + m)}}$$

### Implementation Logic:
1. **Unit Conversion Layer:** To ensure researcher usability, the script accepts **Astronomical Units (AU)** and **Solar Masses ($M_{\odot}$)**.
2. **Standardization:** Internally, inputs are converted to SI (Meters/Kilograms) using:
   - $1 \text{ AU} \approx 1.496 \times 10^{11} \text{ m}$
   - $1 \text{ } M_{\odot} \approx 1.989 \times 10^{30} \text{ kg}$
3. **Execution:** The math is processed using the `math` library for high-precision square roots and powers.

---

## 🛰️ Featured Project: Mission Control Deployment
A decision-tree script that determines the fate of a probe based on calculated gravitational thresholds.

**Threshold Logic:**
* **$v < v_{circular}$**: Sub-orbital trajectory (Atmospheric entry/Crash).
* **$v \approx v_{circular}$**: Stable circular orbit achievement.
* **$v_{circular} < v < v_{escape}$**: Elliptical orbit (Bound state).
* **$v \geq v_{escape}$**: Hyperbolic trajectory (System escape).

---

## 🧪 Validation & Stress Testing
I verified the code against extreme physical regimes to ensure the logic handles various orders of magnitude ($10^6$ to $10^{36}$).

| Object | Context | Input Radius | Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **The Moon** | Planetary Satellite | $3.84 \times 10^8$ m | 27.45 Days | ✅ Passed |
| **51 Pegasi b** | Hot Jupiter | 0.0527 AU | 4.23 Days | ✅ Passed |
| **S2 Star** | Supermassive BH | 1000 AU | 15.37 Years | ✅ Passed |

---

## 💻 Technical Progress (Week 1)
- **Error Handling:** Used `ValueError` exceptions to handle non-numeric inputs.
- **Precision:** Managed floating-point arithmetic for values as small as $G$ ($10^{11}$) and as large as Stellar Masses ($10^{30}$).
- **Environment:** Developed in a local environment, version-controlled via Github, and documented for peer review.

---
**Next Milestone:** Week 2 - Data Wrangling & FITS File Processing.

---
**Author:** Alex
**Date:** May 2026