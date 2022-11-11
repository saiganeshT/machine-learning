from skimage.io import imread
from skimage.color import rgb2gray
from skimage.feature import canny
from detectCircles import *
from getAccumulatorArray import *
from showAccumulatorArray import *
from drawCircle import *
from quantizeAccumulatorArray import *
from numberOfCircles import *

# The filenames you would like to process
file_names = ['egg.jpg', 'jupiter.jpg']
useGradients = [0, 1]
# All the radii you want to check for
radii = [30, 40, 70, 100]
k_value = 3

for file_name in file_names:
  for useGradient in useGradients:
    for radius in radii:
      # get the file name without extension
      name = file_name.split(".")[0]
      # read the input RGB image
      im = imread(file_name)
      # find the centers of the cirlces
      centers = detectCircles(im, radius, useGradient)
      # get the accumulator array 
      accumulator_array = getAccumulatorArray(im, radius, useGradient, name)
      # Draw a cirlce around the strongest radius and save it
      drawCircle(im, centers, radius, name, useGradient)
      # show and save the accumulator array as an image
      showAccumulatorArray(accumulator_array, name, useGradient, radius, normalize = False)

# save the quantized accumulator array
im = imread('egg.jpg')
radius = 70
useGradient = 0
accumulator_array = getAccumulatorArray(im, radius, useGradient, name)
quantized_space = quantizeAccumulatorArray(accumulator_array, k_value)
# get the number of circles from the accumulator array by post-processing the array
num_of_circles = numberOfCircles(accumulator_array)
plt.imshow(accumulator_array)
print(f"The number of predicted circles are {num_of_circles}")
