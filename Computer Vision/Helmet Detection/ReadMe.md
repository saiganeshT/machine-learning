### Abstract
The project aims to evaluate and compare the performance of two popular object detection algorithms, namely Faster R-CNN and Single Shot Detector(SSD), on a helmet detection dataset. The helmet detection task is important for ensuring safety in various scenarios such as construction sites and sports events.

### About Dataset
*Helmet Detection at Work for Safety* dataset from kaggle was used for the project. The dataset followed PASCAL VOC format for annotating bounding boxes. The images are processed by random ﬂipping and distortions.

Size: 1 GB \
Total Data points: 5000 \
Training data : 80% \
Number of Classes : 3 (Helmet, Person, Head)

### An Example Data Point
![example_data_point](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Helmet%20Detection/images/helm_img1.png)

### Implementation steps

1. Setting all dependencies and files required
    1. Installing:
        1. Protocol buffers (for model serialization)
        2. Cocoapi (necessary for TensorFlow Object Detection API)
        3. TensorFlow Object Detection API (contains pre-trained models and helper functions)
    
    2. Downloading:
        1. Helmet detection dataset
        2. Scripts to split, transform, train, and validate our models
        3. Configuration files for our models

    3. Moving and extracting:
        1. All downloaded files and scripts to appropriate locations

2. Setting the workspace
    1. Setting up directories that contain:
        1. Data
        2. Models
        3. Pre-trained models
        4. Checkpoints
    2. Splitting data into different sets
    3. Transforming images and annotations to TFRecords
    4. Splitting large TFRecords into smaller ones that fit into the RAM
    5. Moving downloaded configuration files to their respective directories

3. Training and validation
    1. Running training scripts for both Faster R-CNN and SSD models
    2. Running and stopping validation scripts for both models
    3. Visualizing the results in TensorBoard


### Sample Predictions
![prediction_1](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Helmet%20Detection/images/helm_img2.png)
![prediction_2](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Helmet%20Detection/images/helm_img3.png)
![prediction_3](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Helmet%20Detection/images/helm_img4.png)

### Conclusion
In conclusion, pre-trained models were much more stable during training than blank slate models. This is likely due to the fact that pre-trained models have already been exposed to a wide range of data and have been trained on a variety of tasks, making them more robust and adaptable. In terms of performance, Faster-RCNN has better Precision and recall than SSD, but SSD is more efficient with time. This indicates that the choice of model may depend on the specific requirements of the task at hand. Additionally, data from different sources could have been collected to check the robustness of the model and a more in-depth analysis of both models could have been performed to further compare their strengths and weaknesses. Upon closer examination, the mAP and recall scores do not reflect the results shown in the images and their bounding boxes are very accurate. Therefore, some work needs to be done to adjust the scores

### References
- https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/
- https://www.kaggle.com/code/selmandedeakayoullar/helmet-detection-cnn
- https://neptune.ai/blog/how-to-train-your-own-object-detector-using-tensorflow-object-detection-api
