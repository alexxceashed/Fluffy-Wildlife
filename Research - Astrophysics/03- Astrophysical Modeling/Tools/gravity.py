from celestial_body import CelestialBody
import numpy as np
G = 0.000295912
#Newton's Gravitational Formula 
# G = (g*m1*m2)/r**2


def main():
    cb_A = CelestialBody.get()
    cb_B = CelestialBody.get()
    
    dt = 1.0
    gravity = force(cb_A, cb_B)
    print(gravity)

    for day in range(365):
        current_force = force(cb_A, cb_B)
        cb_B.update(current_force, dt)
        if day % 30 == 0:  # Print every 30 days so the terminal doesn't flood
            print(
                f"Day {day:3d} | Earth Position: X = {cb_B.position[0]:.4f}, Y = {cb_B.position[1]:.4f}"
            )
def force(bodyA, bodyB):
    displacement = bodyA.position - bodyB.position  #Vector3D object
    r = np.linalg.norm(displacement)

    F_mag = (G*bodyA.mass*bodyB.mass)/r
    return F_mag *(displacement/r)

if __name__=="__main__":
    main()