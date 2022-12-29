### Abstract
The project aims to evaluate and compare the performance of two popular object detection algorithms, namely Faster R-CNN and Single Shot Detector(SSD), on a helmet detection dataset. The helmet detection task is important for ensuring safety in various scenarios such as construction sites and sports events.

### About Dataset
*Helmet Detection at Work for Safety* dataset from kaggle was used for the project. The dataset followed PASCAL VOC format for annotating bounding boxes. The images are processed by random ﬂipping and distortions.

Size: 1 GB
Total Data points: 5000
Training data : 80%
Number of Classes : 3 (Helmet, Person, Head)

### An Example Data Point
![example_data_point](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Helmet%20Detection/images/helm_img1.png)

### Implementation steps

1. Setting all dependencies and files required
    1) Installing:
    a) Protocol buffers (for model serialization)
    b) Cocoapi (necessary for TensorFlow Object Detection API)
    c) TensorFlow Object Detection API (contains pre-trained models and helper functions)
    
    2) Downloading:
        a) Helmet detection dataset
        b) Scripts to split, transform, train, and validate our models
        c) Configuration files for our models

    3) Moving and extracting:
        a) All downloaded files and scripts to appropriate locations

2. Setting the workspace
    1) Setting up directories that contain:
        a) Data
        b) Models
        c) Pre-trained models
        d) Checkpoints
    2) Splitting data into different sets
    3) Transforming images and annotations to TFRecords
    4) Splitting large TFRecords into smaller ones that fit into the RAM
    5) Moving downloaded configuration files to their respective directories

3. Training and validation
    1) Running training scripts for both Faster R-CNN and SSD models
    2) Running and stopping validation scripts for both models
    3) Visualizing the results in TensorBoard


### Sample Predictions
![prediction_1](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Helmet%20Detection/images/helm_img2.png)
![prediction_2](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Helmet%20Detection/images/helm_img3.png)
![prediction_3](https://github.com/saiganeshT/machine-learning/blob/main/Computer%20Vision/Helmet%20Detection/images/helm_img4.png)

### Conclusion
- Pre-trained models were much more stable during training than blank slate models.
-Faster-RCNN has better performance in Precision and recall than SSD
-SSD is more eﬃcient with time