import math as m
def main():
    try:
        orbit_calc()
    except KeyboardInterrupt:
        print("Ok\n")
def orbit_calc():
    G = 6.6743*(10**-11)  #Universal Gravitational Constant
    pi = m.pi             #Pi Value
    constants = 2*pi      #Substituted into final result. 
    while True:
        try:
            r_au = float(input("Enter radius(AU): "))   #Asks for radius of planet from star in AU
            #1 AU = 1.4959787 x 10^-11metres
            r = r_au*(1.4959787*(10**11))

            p_sm = float(input("Enter mass of Star(SM):"))
            #1 SM = 1.98847 x 10^30kg
            p_s = p_sm*(1.98847*(10**30))

        except ValueError:
            print("Invalid Entry.")
            continue
        break
    P = (constants*(m.sqrt((r**3)/(G*(p_s)))))
    #1 day = 86400s
    #1 second = 1/86400
    P_EarthDays = P/86400
    P_EarthYears = P_EarthDays/365
    print(f"{P:.3f} seconds or {P_EarthDays:.2f} days or {P_EarthYears:.2f} Earth years.")
main()
