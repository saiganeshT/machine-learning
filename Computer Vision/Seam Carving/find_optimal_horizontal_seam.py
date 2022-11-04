import numpy as np
import scipy
import cv2
from scipy import ndimage
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

def find_optimal_horizontal_seam(cumulativeEnergyMap):

  height = cumulativeEnergyMap.shape[0]
  width = cumulativeEnergyMap.shape[1]

  horizontal_seam = []

  # find the starting point for the horizontal seam
  starting_point_row = np.argmin(cumulativeEnergyMap[:,0])

  # append the starting point
  horizontal_seam.append(starting_point_row)

  col = 0
  
  # 
  while col <= width -2:
    last_min_row = horizontal_seam[-1]

    current_min_row = last_min_row

    # check if the top row exits and check its value against current minimum row
    if (last_min_row-1) >= 0:
      if cumulativeEnergyMap[last_min_row, col+1] > cumulativeEnergyMap[last_min_row-1, col+1]:
        current_min_row = last_min_row-1 

    # check if the bottom row exits and check its value against current minimum row
    if (last_min_row + 1) <= height-1:
      if cumulativeEnergyMap[last_min_row, col+1] > cumulativeEnergyMap[last_min_row+1, col+1]:
        current_min_row = last_min_row+1 

    horizontal_seam.append(current_min_row)
    col += 1

  return horizontal_seam
