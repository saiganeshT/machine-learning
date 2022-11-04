### Goal
To apply Seam Carving and intelligently reduce image size.

### Approach
1. Construct an energy image.
2. Using dynaimc programming, identify the least costly 4-connected path in an image both in horizontal and vertical directions and call them cummulative energy maps.
3. out of all possible paths identify the minimum costly path (**seam**) and remove it.
4. Repeat this process until we reach the desired dimensions to an image.

### Vertical Seam
![vertical seam on an input image](https://raw.githubusercontent.com/saiganeshT/machine-learning/main/Computer%20Vision/Seam%20Carving/images/verticalSeamPrague.png "vertical seam on an input image")

### Horizontal Seam
![horizontal seam on an input image](https://raw.githubusercontent.com/saiganeshT/machine-learning/main/Computer%20Vision/Seam%20Carving/images/horizontalSeamPrague.png "horizontal seam on an input image")

### Normal Resizing v Seam Carving

![original image](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Seam%20Carving/images/tower.jpg "original image")

![reducing width using seam carving](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Seam%20Carving/images/outputReduceWidthTower.png "resized using seam carving")

![normally resized image](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Seam%20Carving/images/resizedTower.png "normally resized image")

