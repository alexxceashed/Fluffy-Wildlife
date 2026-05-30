import numpy as np
import matplotlib.pyplot as plt
masses = []
luminosities = []
def main():
    m,l = mass_range()   #
    plot_graph(m,l)  #passes two lists to function to plot them.
def mass_range():  #function from getting mass from the user, calculates luminosity by using formula and stores both of them in seperate lists.
    while True:
        try:
            mass = float(input("Enter Mass in SM: "))  #inputs mass in SM units, much more usable.
            masses.append(mass)
        except ValueError:
            continue  #continues despite invalid entries.
        except KeyboardInterrupt:
            print("\n")   #print a new line and exit upon Ctrl+C
            break
    for i in range(len(masses)):
        luminosities.append(masses[i]**3.5)
    return masses, luminosities  #returns those lists back to the user to store them.

def plot_graph(x,y):  #plots x,y, with labels and titles.
    plt.style.use('dark_background')  
    plt.plot(x,y,color="white", marker=".", ms=20,mfc="#F2DDD8", lw=3)
    plt.xlabel="Mass"
    plt.ylabel="Luminosity"
    plt.title("Mass vs Luminosity")
    plt.scatter(x,y, color="skyblue", alpha=0.5, s= 50, label ="Luminosity")
    plt.xticks(x)
    plt.yticks(y)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    

main()