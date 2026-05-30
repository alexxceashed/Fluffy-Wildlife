import numpy as np
import matplotlib.pyplot as plt
names = []
temps = []
luminosities = []

def main():
    n,t,l = get_input()
    plot_s(n,t,l)
def get_input():
    while True:
        try:
            INP = input("Enter Name, Temperature(K), and Luminosity:")
            nem, temp, lum = INP.split(",")
            names.append(nem)
            temps.append(float(temp))
            luminosities.append(float(lum))
        except ValueError:
            print("Invalid Entries \n")
            continue
        except KeyboardInterrupt:
            return names,temps,luminosities
def plot_s(naam,garam,roshni):

    calculated_colors = []

    for t in garam:
        if t >= 10000:
            calculated_colors.append('cyan') # Blue/Hot
        elif t >= 5000:
            calculated_colors.append('yellow') # Medium/Sun-like
        else:
            calculated_colors.append('red') # Cool/Red Dwarf or Giant

# Plot using the calculated list
    plt.style.use('dark_background')
    plt.scatter(garam,roshni, label="Stars", color=calculated_colors, s=150)
    # plt.plot(garam,roshni,ls="solid", lw=3, color="white", alpha=0.6)

    line_temps = [30000, 2000]
    line_lums = [10**5, 10**-4]

    # Use plt.plot for the line 
    plt.plot(line_temps, line_lums, color='white', linestyle='--', alpha=0.3, label='Main Sequence Trend')
    plt.gca().invert_xaxis()
    plt.grid(linewidth = 2, color = "lightgray", linestyle = "solid")
    plt.yscale('log')
    for i, txt in enumerate(naam):
        plt.annotate(txt, (garam[i], roshni[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.title("Hertzprung-Russell Diagram")
    plt.xlabel("Temperature")
    plt.ylabel("Luminosity")
    plt.legend()
    plt.show()
main()