import numpy as np

def computeQuantizationError(origImg, quantizedImg):
  error = np.sum((origImg - quantizedImg)**2)
  return error
