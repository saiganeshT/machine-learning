import numpy as np
from skimage.feature import canny
from skimage.io import imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt


def getAccumulatorArray(im, radius, useGradient, name):

  # convert rgb image to grayscale to send it as an input to canny edge detector
  im_gray = rgb2gray(im)
  plt.imsave(f'{name}_gray_image.png', im_gray)

  # get the image of edges from the input image 
  im_edge = canny(im_gray, sigma = 6, low_threshold=0.1)*1
  plt.imsave(f'{name}_edge_image_with_sigma_6.png', im_edge)

  # get the max x and y co-oridnates to create the accumulator array
  height = im_edge.shape[0]
  width = im_edge.shape[1]

  # create the accumulator array and intialize it with zeros
  accumulator_array = np.zeros((height, width))

  # get the gradients and their directions
  gradients = np.gradient(im_edge)
  radians = np.arctan2(gradients[1], gradients[0]) + np.pi # add a pi to change the gradient direction from outside to inside

  # set the polar coordinate resolutions for drawing cirlces around x and y
  resolution = 0.01
  thetas = np.arange(0, 2*np.pi, 0.01)

  # pre-calculate cosines and sines of thetas to avoid calculating for every loop
  cosines = np.cos(thetas)
  sines = np.sin(thetas)

  # for every pixel that is an edge
  for i in range(height):
    for j in range(width):  
      # check if it is an edge
      if im_edge[i, j] != 0:  
        
        # if gradient is to be used to vote get both the angles
        if useGradient == 1:
          PSI = radians[i, j]
          
          # get the theta in the opposite direction too
          PSIs = [PSI, PSI - np.pi]

          # get the a and b co-ordiantes of the cirlce
          a = (j + radius*np.cos(PSIs)).astype('int')
          b = (i + radius*np.sin(PSIs)).astype('int')
        
        # use all the angles 
        else:        
          # get the a and b co-ordiantes of the cirlce
          a = (j + (radius* cosines)).astype('int')
          b = (i + (radius* sines)).astype('int')

        # get the a and b values of the circle coordinates that are inside the range of the image
        valid_a_cor = (a > 0) & (a < (width)) 
        valid_b_cor = (b > 0) & (b < (height))

        valid_a = a[(valid_a_cor & valid_b_cor)]
        valid_b = b[(valid_a_cor & valid_b_cor)]

        # vote in the accumulator array for valid circle coordinates
        accumulator_array[valid_b, valid_a] += 1
  
  return accumulator_array
