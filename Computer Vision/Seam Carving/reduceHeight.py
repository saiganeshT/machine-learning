import numpy as np
import scipy
import cv2
from scipy import ndimage
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
from cumulative_minimum_energy_map import *
from find_optimal_horizontal_seam import *

def reduceHeight(im, energyImage):

  # get the height and width
  height, width = energyImage.shape[0:2]

  # find the cummulative energy map in the horizontal direction for the seam
  cumulativeEnergyMap = cumulative_minimum_energy_map(energyImage, "HORIZONTAL")

  # find the optimal seam
  horizontalSeam = find_optimal_horizontal_seam(cumulativeEnergyMap)

  # reduce the height of image (M, N, 3)
  new_img_list = []
  for i in range(width):
    col = im[:, i, :]
    new_col = np.delete(col, horizontalSeam[i], 0)
    new_img_list.append(new_col)
  reducedColorImage = np.array(new_img_list).transpose(1, 0, 2)#.reshape((height-1, width, 3))

  # reduce the width of energy image (M, N)
  new_ene_img_list = []
  for i in range(width):
    col = energyImage[:, i]
    new_col = np.delete(col, horizontalSeam[i], 0)
    new_ene_img_list.append(new_col)

  reducedEnergyImage = np.array(new_ene_img_list).transpose(1, 0) #reshape((height-1, width))

  return reducedColorImage, reducedEnergyImage
