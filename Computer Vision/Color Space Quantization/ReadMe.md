### Goal
To quantize the color space of RGB and HSV images

### Approach 
**RGB color quantization**
1. Use k-means algorithm to get the mean values of (R, G, B).
2. Create a new array with the same shape as our input image.
3. Fill the pixel values in the new array with the pixel value of the closest k-means cluster center.

_**Input Image**_

![input image](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Color%20Space%20Quantization/images/fish.jpg?raw=true)

_**Results**_

###### with k = 2
![output_image_when_k=2](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Color%20Space%20Quantization/images/quantizedRGB_k_2.png?raw=true)

###### with k = 4
![output_image_when_k=4](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Color%20Space%20Quantization/images/quantizedRGB_k_4.png?raw=true)

###### with k = 8
![output_image_when_k=8](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Color%20Space%20Quantization/images/quantizedRGB_k_8.png?raw=true)


**HSV color quantization**
1. Convert the RGB input image to an HSV image.
2. Get the hue values into a new array.
3. Apply k-means clustering on the new values.
4. Create a new array with the same shape as our input image. 
5. Fill the Saturation and Value channels with the same values as our HSV image.
6. Fill the hue values in the output array with hue values of closest k-means cluster center.

_**Results**_

###### with k = 2
![output_image_when_k=2](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Color%20Space%20Quantization/images/quantizedHSV_with_k_2.png?raw=true)

###### with k = 4
![output_image_when_k=4](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Color%20Space%20Quantization/images/quantizedHSV_with_k_4.png?raw=true)

###### with k = 8
![output_image_when_k=8](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Color%20Space%20Quantization/images/quantizedHSV_with_k_8.png?raw=true)
