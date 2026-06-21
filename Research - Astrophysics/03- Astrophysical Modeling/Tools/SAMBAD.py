from astroquery.vizier import Vizier
from astroquery.simbad import Simbad
import sys

def get():
    return input("Star name: ").strip()

def query(name):
    # SIMBAD for V-magnitude and parallax (distance)
    simbad = Simbad()
    simbad.add_votable_fields("V", "plx")
    result = simbad.query_object(name)

    if result is None:
        print(f"[ERROR] '{name}' not found.")
        sys.exit(1)

    v_mag    = result["V"][0]
    parallax = result["PLX_VALUE"][0]          # milliarcseconds
    distance = 1000 / parallax                 # parsecs (d = 1/p, p in arcsec)

    print(f"\n  Star     : {name}")
    print(f"  V mag    : {v_mag:.3f}")
    print(f"  Parallax : {parallax:.4f} mas")
    print(f"  Distance : {distance:.2f} pc  ({distance * 3.26156:.2f} ly)")

def main():
    name = get()
    query(name)

if __name__ == "__main__":
    main()