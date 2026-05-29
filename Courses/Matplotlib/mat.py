#matplotlib - a plotting library for python
import matplotlib.pyplot as plt
import numpy as np
line_style = dict(marker=".", ms=20, mfc = "cyan",mec ="black", ls="solid", lw=4)
x = np.array([2023,2024,2025,2026])
y1 = np.array([15, 25, 30, 20])  
y2 = np.array([17, 23, 38, 5])  

y3 = np.array([13, 15, 20, 30])  
# plt.style.use('dark_background')
plt.plot(x,y1,color = "black",**line_style) #Multiple markers exist.
plt.plot(x,y2,color = "blue", **line_style) 
plt.plot(x,y3, color = "green", **line_style)
#ms - Marker size
#mfc - Color of the marker, in HEX CODES, or names.
#mec - Marker Edge Color, in HEX CODES, or names. 
#ls - Linestyle, multiple exist, from Documentation
#lw - Line width
plt.show()



#Matplotlib is used in astronomy, physics, engineering, finance, and many other fields to visualize 
# data and create informative graphics. 
# It provides a wide range of plotting functions and customization options, making it a powerful tool 
# for data visualization in Python.
# It is also used to create static, animated, and interactive visualizations in Python.
# Also able to render plots in various formats, including PNG, PDF, SVG, and more.
# Can extract data from .fits file, used in NASA and other space agencies to store astronomical data.
# It is also used in machine learning and data science to visualize data and model performance.