### Goal
To apply hough transform on a given image to detect circular boundaries.

### Algorithm
1. Convert the image to gray scale and apply a Canny edge detector to find the edges of the input image.
2. For every point in the edge image apply gradients and get the angle of the gradients. We will use these angles when the useGradient flag is set.
3. For when the useGradient flag is not set, sample some angles from 360 degrees with equal intervals.
4. For every edge, compute polar coordinates of the circle in hough space using the coordinates of edges, radius and the angles (according to useGradient flag).
5. Filter all the coordinates in the hough space that are outside the range of our image.
6. Then, for all the valid coordinates, increment the accumulator array.
7. After incrementing the accumulator array for every edge pint, get the indices of the accumulator array in the descending order of their values. These are the centers of circles from the strongest to the weakest that fit the image.

### output
**Input Image**

![input image](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Hough%20Transform/Images/egg.jpg?raw=true)

**Edge Image**

![edge image](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Hough%20Transform/Images/egg_edge_image_with_sigma_6.png?raw=true)

**Accumulator Array at radius 70 and when gradients are used**

![accumulator array when gradients are used](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Hough%20Transform/Images/accumulator_array_egg_radius_30_useGradient_1.png?raw=true)

**Image of strongest cirlce (radius @ 70 with gradient)**

![cirlce around egg when radius is 70 and gradient is used](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Hough%20Transform/Images/cirlce_egg_radius_70_useGradient_1.png?raw=true)

**Accumulator Array at radius 70 and when gradients are not used**

![accumulator array when gradients are not used](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Hough%20Transform/Images/accumulator_array_egg_radius_70_useGradient_0.png?raw=true)

**Image of strongest cirlce (radius @ 70 with gradient)**

![cirlce around egg when radius is 70 and gradient is used](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Hough%20Transform/Images/cirlce_egg_radius_70_useGradient_0.png?raw=true)
