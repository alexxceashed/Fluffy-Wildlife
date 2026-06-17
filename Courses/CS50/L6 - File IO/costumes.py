import sys as s
from PIL import Image

images = []
for arg in s.argv[1:]:
    image = Image.open(arg) #this line opens each image file specified in the command line arguments and creates an Image object for each one.
    images.append(image)

images[0].save("costumes.gif", save_all=True, append_images = [images[1]], duration = 200, loop = 0)    
#This line saves the first image in the list as a GIF file named "costumes.gif". 
# The save_all=True parameter indicates that all frames (images) should be saved in the GIF. 
# The append_images parameter specifies the additional images to include in the GIF, starting from the second image in the list. 
# The duration parameter sets the time (in milliseconds) each frame will be displayed, 
# and loop=0 means that the GIF will loop indefinitely.