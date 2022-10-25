import numpy as np
import scipy
import cv2
from scipy import ndimage
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

from energy_image import *
from reduceWidth import *
from find_optimal_vertical_seam import *
from energy_image import *

# reduce the wdith for the first image
im = cv2.imread('inputSeamCarvingPrague.jpg')
energyImage = energy_image(im)

# reduce the width 100 times by 1 pixel at-a-time
for i in range(100):
  reducedColorImage, reducedEnergyImage = reduceWidth(im, energyImage)
  im = reducedColorImage
  energyImage = reducedEnergyImage

# convert BGR color code to RGB color code to before saving the image using matplotlib
im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# save the image
plt.imsave('outputReduceWidthPrague.png', im_rgb)


# reduce the image for the second image
im = cv2.imread('inputSeamCarvingMall.jpg')
energyImage = energy_image(im)

# reduce the width 100 times by 1 pixel at-a-time
for i in range(100):
  reducedColorImage, reducedEnergyImage = reduceWidth(im, energyImage)
  im = reducedColorImage
  energyImage = reducedEnergyImage

# convert BGR color code to RGB color code to before saving the image using matplotlib
im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# save the image
plt.imsave('outputReduceWidthMall.png', im_rgb)
