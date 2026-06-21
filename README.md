# 🌌 Fluffy-Wildlife

Welcome to Fluffy-Wildlife, a learning portfolio combining computer science coursework and applied astrophysics research. This repository was developed largely during summer vacation, and it tracks both structured course practice and experimental scientific coding.

## 📁 Repository Overview

The repository contains these top-level folders:

- `Courses/` — foundational programming coursework and project-based learning.
- `Calculators/` — small standalone calculator scripts.
- `Research - Astrophysics/` — summer vacation astrophysics modules, organized by week.

This README documents each folder in detail, the ideas behind the code, and how the weekly astrophysics modules map to the project structure.

---

## 🎓 Courses

### `Courses/CS50`
This folder contains exercises and exploratory scripts from the Harvard CS50 Python track. It is organized by lecture and concept, so the folder structure reflects a natural learning progression.

Subfolders:
- `L0 - Variables and Functions/` — Python basics, input/output, arithmetic, and simple functions.
- `L1 - Conditionals/` — decision logic with `if`, `elif`, and `else`.
- `L2 - Loops/` — repetition using `for` and `while`, list traversal, and loop patterns.
- `L3  - Exceptions/` — handling errors and validating user input with `try`/`except`.
- `L4 - Libraries/` — importing modules, using packages, and applying library functions.
- `L5 - Unit Tests/` — test-driven practice, writing assertions, and validating code behavior.
- `L6 - File IO/` — reading from and writing to files, plus simple CSV/text handling.
- `L7 - Regular Expressions/` — pattern matching and string validation for text processing.
- `L8 - OOP/` — classes, inheritance, encapsulation, and object-oriented design.

Each CS50 subfolder contains multiple scripts that preserve the learning process and demonstrate the concepts for that week.

### `Courses/Matplotlib`
This folder is dedicated to data visualization practice using `matplotlib`.

Key topics include:
- scatter plots and line plots,
- axis labels, titles, and legends,
- plotting styles and colors,
- scientific chart formatting and presentation.

These examples support the astrophysics research by building visualization literacy.

---

## 🔢 Calculators

### `Calculators/trigonometry.py`
A compact utility for trigonometry calculations. This file is a small reference implementation for using Python math functions and practicing formula-driven programming.

---

## 🚀 Research - Astrophysics

This folder contains the summer astrophysics research work. Each numbered folder corresponds to a weekly module, and the number before each folder name is the week number.

This work was completed during summer vacation, and the folder names serve as module identifiers for the summer learning path. Work is still in progress, and future astrophysics projects created after summer vacation will be stored in new folders to keep post-summer work separate from the summer modules.

### Week mapping

- `01 - Orbital Mechanics` — Week 1 content and foundational mechanics.
- `02- Transit Photometry` — Week 2 content, for working with astronomical data.
- `03- Astrophysical Modeling` — Week 3 content, focusing on reusable models and tools.

> Note: The numbered folder names are project identifiers, and the text of the folder describes the module topic. For example, `02- Transit Photometry` corresponds to the Week 2 module during the summer progression.

### `Research - Astrophysics/01 - Orbital Mechanics`
This module builds the physics foundation for orbital mechanics and defensive scripting.

Contains:
- `Derivations/` — handwritten mathematical derivations and physics notes.
- `Simulations/` — code that generates orbital plots, H-R diagrams, and mission logic.
- `Tools/` — helper scripts such as escape velocity calculators and orbital period formulas.
- `Validation/` — screenshots, graphs, and validations that prove the simulations and formulas work.

This is the most physics-focused module, emphasizing equations, unit conversions, and robust code.

### `Research - Astrophysics/02- Transit Photometry`
This module focuses on transit photometry and exoplanet detection.

Contains:
- `Improved Scripts/` — refined versions of transit search scripts and improved data pipelines.
- `Tools/` — FITS file parsers, light curve plotters, data downloaders, and transit candidate utilities.
- `Validation/` — output screenshots and validation images that show how the pipeline performs.

This section is data-intensive and uses actual astrophysical data formats.

### `Research - Astrophysics/03- Astrophysical Modeling`
This module contains reusable models and interactive tools for astrophysical workflows.

Contains:
- `Objects/` — physics models, such as the `CelestialBody` class.
- `Tools/` — interactive utilities for cleaning FITS light curves (`cleanup.py`), computing cosmological distances (`redshift.py`), querying SIMBAD (`SAMBAD.py`), and simulating gravity (`gravity.py`).

This module is designed to be practical and extensible, with supporting documentation in `Tools/README.md`.

---

## 🧰 AI Usage Warning

AI has only been used to help me understand the code and make the code more efficient. The learning curve was large here, and AI was used to assist me whenever I couldn't seem to get through the problem or the code.

This repository is still my own work, but AI helped clarify concepts, improve structure, and support debugging when needed.

---

## 📌 How to Use This Repository

1. Start with `Courses/CS50` to follow the programming learning progression.
2. Explore `Courses/Matplotlib` for visualization practice.
3. Use `Research - Astrophysics/01 - Orbital Mechanics` for physics modeling and simulation.
4. Use `Research - Astrophysics/02- Transit Photometry` for FITS data and transit detection.
5. Use `Research - Astrophysics/03- Astrophysical Modeling` for reusable physics tools and catalog lookup.

Run scripts from the folder where they are stored to ensure any relative paths resolve properly.

---

## ⚙️ Dependencies

Packages commonly used in this repository:

- `numpy`
- `matplotlib`
- `astropy`
- `astroquery`
- `scipy`
- `wotan`

Install the core environment with:

```bash
python -m pip install numpy matplotlib astropy astroquery scipy wotan
```

---

## 📝 Notes

- The astrophysics work was completed during summer vacation.
- `Research - Astrophysics/02- Transit Photometry` corresponds to Week 4 content even though the folder prefix says `02`.
- `Research - Astrophysics/03- Astrophysical Modeling` includes Week 3-style modeling tools and reusable object code.
- The folder structure was designed to separate learning exercises from research tools.

---

## 📍 Useful starting points

- `Courses/CS50` — programming fundamentals and practice.
- `Courses/Matplotlib` — visualization examples.
- `Research - Astrophysics/01 - Orbital Mechanics` — physics derivations and simulations.
- `Research - Astrophysics/02- Transit Photometry/Tools/README.md` — detailed transit photometry tool instructions.
- `Research - Astrophysics/03- Astrophysical Modeling/Tools/README.md` — detailed guidance for Week 3 utilities.

This README is intended to provide a detailed, high-level overview of the repository and how each folder contributes to the overall portfolio.
