import math as mat
def main():
    try:
        ev_c()  #function for calculating escape velocity
    except KeyboardInterrupt:   #if user wants to terminate program
        print("Ok\n")
def ev_c():
    while True:
        try:
            m = float(input("Enter Mass (kg): "))   #mass of planet in float
            r = float(input("Enter Radius (m): "))  #radius from object to center of earth
        except ValueError:
            print("Invalid Entry")   
            continue
        break
    G = 6.6743 * 10 ** -11  #universal gravitational constant
    v = mat.sqrt((2*G*m)/r) #calculating escape velocity
    v_km = round(v/1000)    #escape velocity in km/s
    print(f"{v:.3f}m/s or {v_km:.2f}km/s")   #outputting velocity in m/s and km/s
main()