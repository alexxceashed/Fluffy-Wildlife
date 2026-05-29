#Grid lines help make plots easier by adding reference lines.
import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5]
y = [5,10,15,20,25]

# plt.xticks(x)
# plt.yticks(y)

plt.grid(linewidth = 2, color = "lightgray", linestyle = "solid") #axis = x or y or both
plt.plot(x,y)
plt.show()
