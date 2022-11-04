import numpy as np
import scipy
import cv2
from scipy import ndimage
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
from energy_image import *
from reduceHeight import *

# reduce the height for the first image
im = cv2.imread('inputSeamCarvingPrague.jpg')
energyImage = energy_image(im)


for i in range(100):
  reducedColorImage, reducedEnergyImage = reduceHeight(im, energyImage)
  im = reducedColorImage
  energyImage = reducedEnergyImage

# convert BGR color code to RGB color code to before saving the image using matplotlib
im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# save the image
plt.imsave('outputReduceHeightPrague.png', im_rgb)


# reduce the height for the second image
im = cv2.imread('inputSeamCarvingMall.jpg')
energyImage = energy_image(im)

for i in range(100):
  reducedColorImage, reducedEnergyImage = reduceHeight(im, energyImage)
  im = reducedColorImage
  energyImage = reducedEnergyImage

# convert BGR color code to RGB color code to before saving the image using matplotlib
im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# save the image
plt.imsave('outputReduceHeightMall.png', im_rgb)
