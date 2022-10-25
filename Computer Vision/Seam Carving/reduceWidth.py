import numpy as np
import scipy
import cv2
from scipy import ndimage
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

from cumulative_minimum_energy_map import *
from find_optimal_vertical_seam import *	

def reduceWidth(im, energyImage):

  # get the height and width
  height, width = energyImage.shape[0:2]

  # find the cummulative energy map in the vertical direction for the seam
  cumulativeEnergyMap = cumulative_minimum_energy_map(energyImage, "VERTICAL")

  # find the optimal seam
  verticalSeam = find_optimal_vertical_seam(cumulativeEnergyMap)

  # reduce the widith of image (M, N, 3)
  new_img_list = []
  for i in range(height):
    row = im[i, :, :]
    new_row = np.delete(row, verticalSeam[i], 0)
    new_img_list.append(new_row)
  reducedColorImage = np.array(new_img_list).reshape((height, width-1, 3))

  # reduce the width of energy image (M, N)
  new_ene_img_list = []
  for i in range(height):
    row = energyImage[i, :]
    new_row = np.delete(row, verticalSeam[i], 0)
    new_ene_img_list.append(new_row)

  reducedEnergyImage = np.array(new_ene_img_list).reshape((height, width-1))

  return reducedColorImage, reducedEnergyImage
