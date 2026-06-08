#Program to input Star Mass and Radius, Transit Depths and Periods to determine the Orbital radius and Planet's size.

import math as m
def main():
    mass,radius,transit_period,transit_depth = get_values()
    print(f"Orbital Radius: {orbital_radius(transit_period, mass)}AU")
    print(f"Planet Radius: {planet_radius(radius, transit_depth)}")

def orbital_radius(tp, sm):
    tp_years = tp/365
    return m.cbrt((tp_years**2)*sm)
def planet_radius(r,td):
    return (r*m.sqrt(td))*9.73
def get_values():
    while True:
        try:
            sm = float(input("Enter Star Mass (SM): "))
            sr = float(input("Enter Radius (R.): "))
            tp = float(input("Enter Transit Period(days): "))
            td = float(input("Enter Transit Depth: "))
        except ValueError:
            print("Invalid Entry")
            continue
        return sm,sr,tp,td
if __name__ == "__main__":
    main()