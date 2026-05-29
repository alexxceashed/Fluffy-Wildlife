import math as m
G = 6.674*(10**-11)
def main():
    while True:
        try:
            planet_mass_SM = float(input("Enter Mass (SM): "))
            planet_mass = 1.989e30*planet_mass_SM
            planet_radius_AU = float(input("Enter Radius(AU): "))
            planet_radius = 1.496e11*planet_radius_AU
            probe_velocity = float(input("Enter Probe Velocity (m/s): "))
        except ValueError:
            print("Invalid Entry")
            continue
        break
    v_e = ev(planet_mass, planet_radius)
    v_c = cv(planet_mass, planet_radius)
    decision_tree = dt(v_e, v_c, probe_velocity)
    if decision_tree == "Crashed":
        print("Insufficient velocity. Probe impacted the surface.")
    elif decision_tree == "Circular":
        print("Stable Circular Orbit achieved!")
    elif decision_tree == "Elliptical":
        print("Elliptical Orbit: Probe is bound but path is elongated.")
    elif decision_tree == "Escape":
        print("Escape Velocity reached. Probe is leaving the system")
def ev(pm, pr):
    return m.sqrt((2*G*pm)/pr)
def cv(ppm, ppr):
    return m.sqrt((G*ppm)/ppr)

def dt(escape_v, circular_v, p_v):
    if circular_v > p_v:
        return "Crashed"
    elif p_v <= circular_v*1.01 and p_v >= circular_v*0.99:
        return "Circular"
    elif circular_v < p_v < escape_v:
        return "Elliptical"
    elif p_v >= escape_v:
        return "Escape"
main()