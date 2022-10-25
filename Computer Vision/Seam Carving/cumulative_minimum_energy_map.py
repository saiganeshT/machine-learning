import numpy as np
import scipy
import cv2
from scipy import ndimage
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

# function to compute commulative minimum energy of a given energy image
def cumulative_minimum_energy_map(energyImage, seamDirection):
  
  cum_min = np.zeros_like(energyImage)
  height = cum_min.shape[0]
  width = cum_min.shape[1]

  if seamDirection == "HORIZONTAL":
    
    # fill the last column to be last column of the energyImage as it is the minimum  
    cum_min[:, -1] = energyImage[:, -1]
    
    # Iterate from the right (excluding the last column) to the left columns, from top to bottom rows and fill the minimum values
    for col in range(width-2, -1, -1):
      for row in range(0, height):
        
        if row-1 >= 0 and row+1 <= height-1:
          cum_min[row, col] = energyImage[row, col] + min( cum_min[row-1, col+1], cum_min[row, col+1], cum_min[row+1, col+1])
        elif row-1 < 0:
          cum_min[row, col] = energyImage[row, col] + min( cum_min[row, col+1], cum_min[row +1, col+1])
        elif row+1 > height-1:
          cum_min[row, col] = energyImage[row, col] + min( cum_min[row-1, col+1], cum_min[row, col+1])


  elif seamDirection == "VERTICAL":
    
    # fill the last row to be last row of the energyImage as it is the minimum  
    cum_min[-1, :] = energyImage[-1,:]

    # Iterate from the bottom (excluding the last row) to the top rows, from left to right columns and fill the minimum values
    for row in range(height-2, -1, -1):
      for col in range(0, width):
        
        if col-1 >= 0 and col+1 <= width-1:
          cum_min[row, col] = energyImage[row, col] + min( cum_min[row+1, col-1], cum_min[row+1, col], cum_min[row+1, col+1])
        elif col-1 < 0:
          cum_min[row, col] = energyImage[row, col] + min( cum_min[row+1, col], cum_min[row +1, col+1])
        elif col+1 > width-1:
          cum_min[row, col] = energyImage[row, col] + min( cum_min[row+1, col-1], cum_min[row+1, col])
  
  else:
      print("Enter valid seamDirection")
      exit(1)

  cum_min = (cum_min / np.max(cum_min))*255

  return cum_min
