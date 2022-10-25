import numpy as np
import scipy
import cv2
from scipy import ndimage
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

def find_optimal_vertical_seam(cumulativeEnergyMap):

  height = cumulativeEnergyMap.shape[0]
  width = cumulativeEnergyMap.shape[1]

  vertical_seam = []

  # find the starting point for the vertical seam
  starting_point_col = np.argmin(cumulativeEnergyMap[0,:])

  # append the starting point
  vertical_seam.append(starting_point_col)

  row = 0
  
  # 
  while row <= height -2:
    last_min_col = vertical_seam[-1]

    current_min_col = last_min_col

    # check if the left col exits and check its value against current minimum col
    if (last_min_col-1) >= 0:
      if cumulativeEnergyMap[row+1, last_min_col] > cumulativeEnergyMap[row+1, last_min_col-1]:
        current_min_col = last_min_col-1 

    # check if the right col exits and check its value against current minimum col
    if (last_min_col + 1) <= width-1:
      if cumulativeEnergyMap[row+1, last_min_col] > cumulativeEnergyMap[row+1, last_min_col+1]:
        current_min_col = last_min_col+1 

    vertical_seam.append(current_min_col)
    row += 1

  return vertical_seam
