# import all the necessar libraries
import numpy as np
from sklearn.cluster import KMeans
from skimage.color import rgb2hsv, hsv2rgb

def quantizeHSV(origImg, k):

  # convert rgb image to hsv image
  hsvImg = rgb2hsv(origImg)

  # get the hue values from hsv image
  hue = hsvImg[:,:,0].reshape((-1,1))

  # fit the KMeans on hue values 
  kmeans = KMeans(n_clusters=k).fit(hue)

  # get the centroids 
  meanHues = kmeans.cluster_centers_

  # get the predictions for hue values
  predictions = kmeans.predict(hue)

  # fill the outputimage
  outputImg = np.zeros_like(hsvImg)

  # fill the saturation and values in the output image
  outputImg[:, :, 1] = hsvImg[:, :, 1]
  outputImg[:, :, 2] = hsvImg[:, :, 2]

  pointer = 0

  for height in range(outputImg.shape[0]):
    for width in range(outputImg.shape[1]):
      outputImg[height, width, 0] = meanHues[predictions[pointer]]
      pointer += 1

  # convert HSV image back to RGB image
  outputImg = hsv2rgb(outputImg)
  
  return outputImg, meanHues
