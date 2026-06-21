import math
import re
import numpy as np
# class Vector3D: #It has 3 coordinates: x, y, z. All 3 axis operate independently of each other.
#     def __init__(self,x=0.0,y=0.0,z=0.0): #By defualt, position at center of origin.
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         z = self.z + other.z
#         return Vector3D(x,y,z)
#     def __sub__(self, other):
#         x = self.x - other.x
#         y = self.y - other.y
#         z = self.z - other.z
#         return Vector3D(x,y,z)
    
#     def magnitude(self):
#         return math.sqrt(self.x**2 + self.y**2 + self.z**2)
class CelestialBody: 
    def __init__(self,name,velocity=np.array([0, 0, 0]),position=np.array([0,0,0]),mass=1,radius=0.00465):
        #mass and radius will be measured in Sm and AU units respectively.
        #because metric units like kg, metres, will be too small for such a large
        #scale.
        self.velocity = velocity
        self.position = position
        self.mass = mass
        self.radius = radius
        self.name = name
    
    def __str__(self):
        return f"Mass of {self.name}: {self.mass}M. \nRadius of {self.name}: {self.radius}R."
    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, m):
        if m < 0:
            raise ValueError("Invalid CelestialBody Mass.")
        elif (10**-12) > m:
            raise ValueError("This is basically spacedust!")
        elif 5e10 < m:
            raise ValueError("Supermassive BlackHole Detected. You broke Physics!")
        self._mass = m


    @property 
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, r):
        if 10**-7 > r:
            raise ValueError("Absolute Lower Limit surpassed.")
        if 100.0 < r:
            raise ValueError("Supermassive BlackHole Detected. You broke Physics!")
        self._radius = r
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        position = cls.input_vector("Position Vector(x,y,z): ")
        velocity = cls.input_vector("Velocity Vector(vx,vy,vz): ")
        while True:
            try:
                mass = float(input("Mass: "))
                
            except ValueError:
                print("Invalid Mass, try again!")
                continue
            break
        while True:
            try:
                radius = float(input("Radius: "))
                
            except ValueError:
                print("Invalid Radius, try again!")
                continue
            break
        return cls(name, velocity, position, mass, radius)
     
    @classmethod
    def input_vector(cls, string):
        while True:
            pattern = r"([-+]?\d+(?:\.\d+)?)\s*,\s*([-+]?\d+(?:\.\d+)?)\s*,\s*([-+]?\d+(?:\.\d+)?)"
            if matches:= re.search(pattern, input(string)):
                x,y,z = matches.groups()
                return np.array([float(x), float(y), float(z)])
            else:
                print("Invalid Vector format. Please try again.")
                continue
    
    def update(self, force_vector, dt):
        """
        Updates the 3D position and velocity arrays of the celestial body
        using Newton's laws of motion and NumPy vector math.
        
        force_vector: A 1D NumPy array [Fx, Fy, Fz] acting on this body.
        dt: The time step slice (in days) for this simulation step.
        """
        # 1. Acceleration vector = Force vector / mass (A = F / m)
        acceleration = force_vector / self.mass
        
        # 2. Update velocity vector (V_new = V_old + A * dt)
        self.velocity += acceleration * dt
        
        # 3. Update position vector (P_new = P_old + V * dt)
        self.position += self.velocity * dt
