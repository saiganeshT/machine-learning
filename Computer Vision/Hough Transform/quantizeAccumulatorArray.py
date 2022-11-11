import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def quantizeAccumulatorArray(accumulator_array, k_value):
  accumulator_array1D = accumulator_array.reshape(-1,1)

  # fit a kmeans cluster on the accumulator array
  kmeans = KMeans(n_clusters=k_value).fit(accumulator_array1D)

  # get the centroids
  meanVotes = kmeans.cluster_centers_

  # get the predictions on our space
  predictions = kmeans.predict(accumulator_array1D)

  #fill the output accumulator array
  quantizedArray = np.zeros_like(accumulator_array)

  pointer = 0

  for height in range(accumulator_array.shape[0]):
    for width in range(accumulator_array.shape[1]):
      quantizedArray[height, width] = meanVotes[predictions[pointer]]
      pointer += 1

  plt.imsave("quantizedAccumulatorArray.png", quantizedArray.astype('uint8'))
  return quantizedArray
