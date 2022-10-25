import numpy as np
import scipy
import cv2
from scipy import ndimage
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

# function to compute enery of a given image
def energy_image(im):

  image = im.astype('uint8')

  # convert the BGR image to gray scale image
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # horizontal derivative using SOBEL filter
  dx = ndimage.sobel(gray, 0)

  # vertical derivative using SOBEL filter
  dy = ndimage.sobel(gray, 1)

  # compute the magniture of derivatives
  energy = np.hypot(dx, dy)

  # normalize the energy to be in the [0, 255]

  energy *= 255.0 / np.max(energy)

  # convert the data type to double
  energy = energy.astype('float64')

  return energy
