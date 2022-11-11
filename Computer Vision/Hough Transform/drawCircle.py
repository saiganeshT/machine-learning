import numpy as np
import matplotlib.pyplot as plt
import cv2

def drawCircle(im, centers, radius, name, use_gradient):
  
  # get the best center
  (height, width) = centers[0]
  # draw the circle over the image 
  output_img = cv2.circle(im, (width, height), radius, (255, 0, 0))
  # save the image
  plt.imsave(f"cirlce_{name}_radius_{radius}_useGradient_{use_gradient}.png",output_img.astype('uint8'))
  plt.imshow(output_img)
