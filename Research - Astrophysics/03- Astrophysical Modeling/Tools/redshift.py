from astropy.cosmology import Planck18 as cosmo
from astropy import units as u
def main():
    while True:
        try:
            redshift = float(input("Enter redshift: "))
            if redshift < 0:
                print("Enter Valid Redshift(z).")
        except ValueError:
            print("Invalid Input. Try again")
            continue
        break
    print(calculation(redshift))
def calculation(z):
    age = cosmo.age(z).value
    current_age = cosmo.age(0).value
    actual_distance = cosmo.comoving_distance(z).value
    optical_distance = cosmo.luminosity_distance(z).value
    lookback_age = current_age-age

    return (
        f"Redshift: {z}\n"
        f"Age of Universe at Emission: {age:.2f} Billion Years\n"
        f"Lookback Time (Light Travel Time): {lookback_age:.2f} Billion Years\n"
        f"Comoving Distance (Current Physical Distance): {actual_distance * 3.26156e6:.2e} Light-Years\n"
        f"Luminosity Distance (Apparent Distance): {optical_distance * 3.26156e6:.2e} Light-Years"
    )

if __name__ == "__main__":
    main()