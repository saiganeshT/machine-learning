import numpy as np
import matplotlib.pyplot as plt

def showAccumulatorArray(accumulator_array, name, use_gradient, radius, normalize = False):

  if normalize:
    min = np.min(accumulator_array)
    max = np.max(accumulator_array)
    accumulator_array = ((accumulator_array - min)/(max - min)) * 255

  plt.imsave(f"accumulator_array_{ name }_radius_{radius}_useGradient_{use_gradient}.png",accumulator_array.astype('uint8'))
  plt.imshow(accumulator_array.astype('uint8'))

