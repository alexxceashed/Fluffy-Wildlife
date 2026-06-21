# Validation

This folder contains validation evidence for the `03 - Astrophysical Modeling` tools.

The current validation scope covers the `Tools/gravity.py` scenario where:

- the star is held fixed in place,
- the planet is updated using the modeled gravitational force,
- the simulation runs for 365 daily time steps,
- the output values were verified against the intended scenario behavior.

## Validation status

- ✅ `Tools/gravity.py` successfully passed the intended fixed-star scenario validation.
- ✅ The `Tools/README.md` now documents that the star remains fixed while the planet moves.

This folder is intended as the home for additional test artifacts and evidence as further validation work is completed.
