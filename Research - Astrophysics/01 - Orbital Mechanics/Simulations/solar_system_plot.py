import matplotlib.pyplot as plt
# 1. Data (AU and Years)
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
distances = [0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06] # a
periods = [0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8] # P

# 2. Setup the Plot
plt.style.use('dark_background') # Makes it look like space!
plt.figure(figsize=(10, 6))

# 3. Create the Scatter Plot
plt.scatter(distances, periods, color='cyan', edgecolors='white', s=100, label='Planets')

# 4. Customization (Apply what you learned!)
plt.title("Kepler's Third Law: Distance vs. Period")
plt.xlabel("Semi-Major Axis (AU)")
plt.ylabel("Orbital Period (Years)")
plt.grid(linestyle='--', alpha=0.5)

# 5. THE MAGIC STEP: Make it Logarithmic
# This turns the curve into a straight line, proving the P^2 = a^3 relationship
plt.xscale('log')
plt.yscale('log')

# 6. Annotate (Optional: label the dots)
for i, txt in enumerate(planets):
    plt.annotate(txt, (distances[i], periods[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.legend()

#AI was used in this project as to introduce me to the basics of plotting.
plt.show()
plt.savefig('kepler_plot.png')