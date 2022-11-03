# import all the necessar libraries
import numpy as np
from sklearn.cluster import KMeans

# function to quantize RGB values in an image
def quantizeRGB(origImg, k):

  # convert the 3D array of (H, W, C) to a 2D array of (H*W, C)
  origImg2D = origImg.reshape((-1, 3))

  # fit a kmeans cluster on the image
  kmeans = KMeans(n_clusters=k).fit(origImg2D)

  # get the centroids
  meanColors = kmeans.cluster_centers_

  # get the predictions on our image
  predictions = kmeans.predict(origImg2D)

  #fill the outputimage
  outputImg = np.zeros_like(origImg)

  pointer = 0

  for height in range(outputImg.shape[0]):
    for width in range(outputImg.shape[1]):
      outputImg[height, width] = meanColors[predictions[pointer]]
      pointer += 1

  return outputImg, meanColors
