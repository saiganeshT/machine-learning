import numpy as np
import scipy
import cv2
from scipy import ndimage
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

def displaySeam(im, seam, type):

  # seam visualization color (BGR)
  SEAM_COLOR = [255, 0, 0]

  height, width = im.shape[0:2]

  if type == 'VERTICAL':
    for row in range(height):
      im[row, seam[row], : ] = SEAM_COLOR

    # convert BGR color code to RGB color code to display the image using matplotlib
    im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    plt.imsave('verticalSeamPrague.png', im_rgb)
    plt.imshow(im_rgb)
    plt.show()

  elif type == 'HORIZONTAL':
    for col in range(width):
      im[seam[col], col, :] = SEAM_COLOR

    # convert BGR color code to RGB color code to display the image using matplotlib
    im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    plt.imsave('horizontalSeamPrague.png', im_rgb)
    plt.imshow(im_rgb)
    plt.show()
