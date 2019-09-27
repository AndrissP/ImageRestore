##import skimage.io
##import numpy as np
##import skimage.viewer
##from matplotlib import pyplot as plt
##import sys
##
###Intensity matrix
##I = skimage.io.imread('image.png',as_grey=True).astype(np.float32)
##plt.imshow(I, cmap='gray', interpolation='nearest');
##plt.savefig('./Results/file.png')  


from PIL import Image
import numpy as np
import sys
from matplotlib import pyplot as plt
img = Image.open('Pics\serveimage.jpg').convert('L')
img2=Image.open('Pics\serveimage.jpg')
img.save('greyscale.jpg')
#img2.save(r"GrayFig.jpg")
