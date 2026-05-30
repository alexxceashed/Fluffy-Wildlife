import math as m
G = 6.674*(10**-11)
def main():
    while True:
        try:
            planet_mass_SM = float(input("Enter Mass (SM): "))   #Prompts User for Mass in SolarMass Units
            planet_mass = 1.989e30*planet_mass_SM #Converts SM to Metric Unit(kg) for calculations
            planet_radius_AU = float(input("Enter Radius(AU): ")) #Prompts User for Radius in Astronomical Units
            planet_radius = 1.496e11*planet_radius_AU #Converts AU to Metric Unit(m) for calculations
            probe_velocity = float(input("Enter Probe Velocity (m/s): "))  #Prompts Probe Velocity to determine it's fate.
        except ValueError:
            print("Invalid Entry")
            continue
        break
    v_e = ev(planet_mass, planet_radius)   #calls ev function to calculate escape velocity of the object by passing in mass and radius of the planet.
    v_c = cv(planet_mass, planet_radius)   #calls cv function to calculate circular velocity of the object by passing in mass and radius of the planet
    decision_tree = dt(v_e, v_c, probe_velocity) #calls dt function to determine fate of the probe, and prints it.
    if decision_tree == "Crashed":
        print("Insufficient velocity. Probe impacted the surface.")
    elif decision_tree == "Circular":
        print("Stable Circular Orbit achieved!")
    elif decision_tree == "Elliptical":
        print("Elliptical Orbit: Probe is bound but path is elongated.")
    elif decision_tree == "Escape":
        print("Escape Velocity reached. Probe is leaving the system")
def ev(pm, pr):  #returns escape velocity using formula.
    return m.sqrt((2*G*pm)/pr)
def cv(ppm, ppr): #returns circular velocity using formula.
    return m.sqrt((G*ppm)/ppr)

def dt(escape_v, circular_v, p_v):   #takes in 3 arguements, escape velocity, circular velocity and probe velocity. makes comparisions between these 3 and determines it's fate.
    if circular_v > p_v:
        return "Crashed"
    elif p_v <= circular_v*1.01 and p_v >= circular_v*0.99:
        return "Circular"
    elif circular_v < p_v < escape_v:
        return "Elliptical"
    elif p_v >= escape_v:
        return "Escape"
main()