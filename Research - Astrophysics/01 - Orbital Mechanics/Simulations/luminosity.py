import numpy as np
import matplotlib.pyplot as plt
masses = []
luminosities = []
def main():
    m,l = mass_range()
    plot_graph(m,l)
def mass_range():
    while True:
        try:
            mass = float(input("Enter Mass in AU: "))
            masses.append(mass)
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("\n")
            break
    for i in range(len(masses)):
        luminosities.append(masses[i]**3.5)
    return masses, luminosities

def plot_graph(x,y):
    plt.style.use('dark_background')
    plt.plot(x,y,color="white", marker=".", ms=20,mfc="#F2DDD8", lw=3)
    plt.title("Mass vs Luminosity")
    plt.scatter(x,y, color="skyblue", alpha=0.5, s= 50, label ="Luminosirt")
    plt.xticks(x)
    plt.yticks(y)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    

main()