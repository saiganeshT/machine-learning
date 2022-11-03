import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2hsv
from quantizeRGB import *
from quantizeHSV import *
from computeQuantizationError import *
from getHueHists import *

#def colorQuantizeMain.py:

origImg = io.imread('fish.jpg')
hsv_image = rgb2hsv(origImg)


for k in [2, 4, 8]:
  quantizedRGBImg, meanColors = quantizeRGB(origImg, k)
  plt.imsave(f"quantizedRGB_k_{k}.png", quantizedRGBImg)
  RGBerror = computeQuantizationError(origImg, quantizedRGBImg)
  quantizedHSVImg, meanHues = quantizeHSV(origImg, k)
  plt.imsave(f"quantizedHSV_with_k_{k}.png", quantizedHSVImg)
  HSVerror = computeQuantizationError(hsv_image, quantizedHSVImg)
  getHueHists(origImg, k)
  print(f"For K = {k}:\n\tRGB error is: {int(RGBerror)}\n\tHSV error is: {int(HSVerror)}")

