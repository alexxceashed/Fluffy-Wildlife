import numpy as np
import matplotlib.pyplot as plt
names = []
temps = []
luminosities = []

def main():
    n,t,l = get_input()   #stores all 3 variables in lists.
    plot_s(n,t,l)   #passes those 3 variables to the function to plot them on graph.
def get_input():   #function that gets the names, temperatures, and luminosities of the stars and stores them in lists, and returns them.
    while True:
        try:
            INP = input("Enter Name, Temperature(K), and Luminosity:")   
            nem, temp, lum = INP.split(",")   #splitting the input into 3 seperate entities.
            names.append(nem) #appending those entities to lists.
            temps.append(float(temp))
            luminosities.append(float(lum))
        except ValueError:
            print("Invalid Entries \n")  #Catches ValueError and prompts user to write correct entries
            continue
        except KeyboardInterrupt:
            return names,temps,luminosities   #on exit, return lists.
def plot_s(naam,garam,roshni):  #function to plot the temperatures and luminosities of the stars using matplotlib.

    calculated_colors = []   #empty list for storin colors

    for t in garam:   #decides the color of the scatter dots of each star relative to its temperature.
        if t >= 10000:
            calculated_colors.append('cyan') # Blue/Hot
        elif t >= 5000:
            calculated_colors.append('yellow') # Medium/Sun-like
        else:
            calculated_colors.append('red') # Cool/Red Dwarf or Giant

# Plot using the calculated list
    plt.style.use('dark_background')  #dark background
    plt.scatter(garam,roshni, label="Stars", color=calculated_colors, s=150)
    # plt.plot(garam,roshni,ls="solid", lw=3, color="white", alpha=0.6)

    line_temps = [30000, 2000]
    line_lums = [10**5, 10**-4]

    # Use plt.plot for the line 
    plt.plot(line_temps, line_lums, color='white', linestyle='--', alpha=0.3, label='Main Sequence Trend')
    plt.gca().invert_xaxis() #invert x axis, as h-r diagram represents hot stars in the right and cold stars in the left.
    plt.grid(linewidth = 2, color = "lightgray", linestyle = "solid")
    plt.yscale('log')  #log scale, as exponential measurements are present.
    for i, txt in enumerate(naam):
        plt.annotate(txt, (garam[i], roshni[i]), textcoords="offset points", xytext=(0,10), ha='center')  #annotate each star's name side by side(AI used.)
    plt.title("Hertzprung-Russell Diagram")  #Title of the diagram.
    plt.xlabel("Temperature")
    plt.ylabel("Luminosity")
    plt.legend()   #Labels assigned.
    plt.show()
main()