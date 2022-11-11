import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2hsv
from quantizeHSV import *


def getHueHists(im, k):

  hsv_img = rgb2hsv(im)
  im_hue_values = np.ravel(hsv_img[:, :, 0])
  histEqual = plt.hist(im_hue_values)

  outputImg, meanHues = quantizeHSV(im, k)
  outputImg = rgb2hsv(outputImg)
  clustered_hue_values = np.ravel(outputImg[:, :, 0])
  histClustered = plt.hist(clustered_hue_values)
  
  fig, ax = plt.subplots(1, 2, figsize=(10,7))
  ax[0].hist(im_hue_values, bins = k)
  ax[0].title.set_text("Histogram with original Hue values")
  ax[1].hist(clustered_hue_values)
  ax[1].title.set_text("Histogram with Clustered Hue values")

  fig.savefig(f'hist with k = {k}.png')

  return histEqual, histClustered
