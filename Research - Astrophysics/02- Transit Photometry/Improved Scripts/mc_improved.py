import math as m
import sys as s
UNIVERSAL_GRAVITATIONAL_CONSTANT = 6.67 * (10**-11)
c = 299792458

def main():
    Mass,Radius,Velocity = values()
    CVelocity,EVelocity = calculator(Mass,Radius)
    outcome = decide(Velocity,EVelocity, CVelocity)
    print(outcome)
    

def decide(PVelocity, EVelocity, CVelocity):
    # 1. The Perfect Circle 
        if PVelocity >= CVelocity * 0.99 and PVelocity <= CVelocity * 1.01:
            return """🔵 MISSION SUCCESS: STABLE CIRCULAR ORBIT
   -> Telemetry: Target velocity perfectly matches planetary gravity.
   -> Physics: The probe's kinetic energy perfectly balances the gravitational pull at this altitude. It will continuously "fall" around the planet in a perfectly round, stable orbit."""

# 2. The Edge of Escape (Parabolic)
        elif PVelocity >= EVelocity * 0.99 and PVelocity <= EVelocity * 1.01:
            return """🟡 MISSION WARNING: PARABOLIC TRAJECTORY ACHIEVED
   -> Telemetry: Probe is at exactly 100% of the required escape velocity.
   -> Physics: The probe has precisely the minimum energy needed to break free. It will coast outward forever, its speed continuously slowing down and approaching zero as it reaches deep space."""

# 3. The Crash (Sub-Orbital)
        elif PVelocity < CVelocity:
            return """🔴 MISSION FAILURE: SUB-ORBITAL IMPACT IMMINENT
   -> Telemetry: Probe velocity is below the minimum circular threshold.
   -> Physics: The probe lacks the necessary lateral speed (kinetic energy) to "miss" the ground as it falls. Planetary gravity has overpowered the probe, resulting in a surface crash."""

# 4. The Oval (Elliptical)
        elif CVelocity < PVelocity < EVelocity:
            return """🟢 MISSION SUCCESS: STABLE ELLIPTICAL ORBIT
   -> Telemetry: Probe is captured, but velocity exceeds circular threshold.
   -> Physics: The probe has enough energy to stretch its orbit into an oval. It will swing far out into space (apoapsis) before gravity pulls it back in fast and close to the planet (periapsis)."""

# 5. The Deep Space Escape (Hyperbolic)
        elif PVelocity > EVelocity:
            return """🟣 MISSION OUTCOME: SYSTEM ESCAPE (HYPERBOLIC)
   -> Telemetry: Probe velocity vastly exceeds planetary binding energy.
   -> Physics: The planet's gravity will bend the probe's flight path, but the probe is moving too fast to be captured. It will slingshot past the planet and permanently leave the system."""
def calculator(Mass,Radius):
    CVelocity = m.sqrt((UNIVERSAL_GRAVITATIONAL_CONSTANT*Mass)/Radius)
    EVelocity = CVelocity * m.sqrt(2)
    return CVelocity, EVelocity
def values():
    while True:
        try:
            M = float(input("Enter Mass (Solar Masses): "))
            M_SI = M*1.989e30
            R = float(input("Enter Radius(Astronomical Units): "))
            R_SI = R*1.496e11
            S_R = (2*UNIVERSAL_GRAVITATIONAL_CONSTANT*M_SI)/(c**2)
            V = float(input("Enter Probe Velocity (m/s): "))

            if M <= 0 or R <= 0:
                print("\nERROR: Mass/Radius cannot be 0 or Negative.\n")
                raise ValueError
            elif V < 0:
                print("\nERROR: Probe Velocity cannot be Negative.")
                raise ValueError
            elif V > 299792458:
                print("\nERROR: Probe Velocity cannot be greater than SOL")
                raise ValueError
            elif R_SI <= S_R:
                print("Mass is too DENSE! Collapsing into Black Hole.")
                raise ValueError
            elif M_SI > 2.467e28:
                print("\nERROR: This mass is large enough to trigger nuclear fusion. This is a star, not a planet!")
                raise ValueError
        except ValueError:
            continue
        except KeyboardInterrupt:
            s.exit("Cancelled.")
        break
    return M_SI,R_SI,V
main()