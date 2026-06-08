# mc_improved.py

`mc_improved.py` is an enhanced orbital trajectory assessment script for transit photometry and astrophysics exploration. It reads a probe velocity and a planetary mass/radius description from the user, computes circular and escape velocities, and returns a mission outcome message with clear physics reasoning.

## Features

- Converts user inputs from Solar Masses and Astronomical Units into SI units.
- Computes both circular orbit velocity and escape velocity.
- Classifies the probe trajectory with five outcomes:
  - Stable circular orbit
  - Parabolic escape trajectory
  - Sub-orbital impact (crash)
  - Elliptical orbit
  - Hyperbolic escape
- Detects and rejects impossible or invalid input values:
  - non-positive mass or radius
  - negative probe velocity
  - probe velocity above the speed of light
  - object so dense it would collapse into a black hole
  - object massive enough to be a star instead of a planet
- Uses user-friendly error handling and retry loops.

## Usage

Run the script with Python and follow the prompts:

```bash
python mc_improved.py
```

Then provide:

1. Mass in Solar Masses
2. Radius in Astronomical Units
3. Probe velocity in meters per second

## Inputs

- `Mass` in Solar Masses
- `Radius` in Astronomical Units
- `Probe Velocity` in meters per second

## Outputs

- A detailed mission result string describing whether the probe is in a circular orbit, elliptical orbit, escape trajectory, or will crash.
- Physics-based explanations for the chosen outcome.

## Improvements over `mission_control.py`

`mc_improved.py` is a more robust and realistic version of the earlier `mission_control.py`. It improves on the original in these ways:

- Better input validation and retry handling
- Rejects impossible physics cases (black hole formation, stellar mass, velocity above light speed)
- Uses consistent SI unit conversion from astrophysical input units
- Provides richer, descriptive mission outcome messages
- More modular structure with separate functions for values, calculation, and decision logic
- Expanded decision categories, including parabolic and hyperbolic outcomes

## Notes

This script is intended for educational use and simple orbit classification. It does not simulate orbital dynamics over time, but it does compare energy thresholds that determine common trajectory classes.
