### Abstract
The project aims to evaluate and compare the performance of two popular object detection algorithms, namely Faster R-CNN and Single Shot Detector(SSD), on a helmet detection dataset. The helmet detection task is important for ensuring safety in various scenarios such as construction sites and sports events.

### About Dataset
*Helmet Detection at Work for Safety* dataset from kaggle was used for the project. The dataset followed PASCAL VOC format for annotating bounding boxes. The images are processed by random ﬂipping and distortions.

Size: 1 GB
Total Data points: 5000
Training data : 80%
Number of Classes : 3 (Helmet, Person, Head)

### An Example Data Point
![example_data_point]()

### Sample Predictions
![prediction_1]()
![prediction_2]()
![prediction_3]()

### Conclusion
- Pre-trained models were much more stable during training than blank slate models.
-Faster-RCNN has better performance in Precision and recall than SSD
-SSD is more eﬃcient with time