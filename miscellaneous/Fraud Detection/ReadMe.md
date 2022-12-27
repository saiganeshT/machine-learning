### Research Question

Fraudulent transaction detection is a critical problem in the financial industry, as it can have serious consequences for both businesses and consumers. In this project, we explore a variety of different algorithms, including logistic regression, support vector machines, and neural networks, and compare their performance in terms of accuracy and speed on a dataset of labeled transactions. We also investigate the use of different evaluation metrics, such as precision and recall, to assess the performance of the models on imbalanced data. The results of our study provide insights into the effectiveness of different classification algorithms for fraudulent transaction detection and may serve as a useful reference for practitioners in the field.

### Dataset

The sample size is 284,807 and there are 30 features. The data is highly imbalanced with significantly higher non-fraudulent labels. The features are processed by the vendor for security purposes using PCA, therefore, all the features are numerical.


### ML Methodology

Overview of algorithms

_Logistic regression_ is a classification algorithm that uses a linear combination of features to predict the probability that an input belongs to a certain class. It does this by using the logistic function to map the predicted probability to a value between 0 and 1. \

_Support vector machines_ (SVMs) are a type of supervised learning algorithm that can be used for classification or regression tasks. They work by finding the hyperplane in a high-dimensional space that maximally separates the different classes. \

_AdaBoost_ (Adaptive Boosting) is an ensemble learning algorithm that combines multiple weak learners to form a strong learner. It works by iteratively training weak learners on weighted versions of the training data, with more weight given to misclassified examples.\

A _multi-layer perceptron_ (MLP) is a type of neural network that consists of multiple layers of artificial neurons, with the input layer receiving the input data, hidden layers processing it, and the output layer providing the final prediction. It works by adjusting the weights of the connections between neurons based on the error between the predicted and actual output.\

### Reasons for the choosing these
_Logistic Regression_: This simple method is used to establish a baseline\
_Ensemble_: This popular technique is used to compare how they compare against neural networks in an unbalanced data setting.\
_SVM_: This too along with Logistic Regression is used to establish a baseline.\
_Multi-Layer Perceptron_: To test whether they generalize well with unbalanced data or
succumb overfitting.\

### Use of the dataset
The label column of the dataset has been used as our target variable and all the rest of the columnas are used as features.

Splits\
   Training: 60%\
   Validation: 20%\
   Testing: 20%\

### Preprocessing
There is no need to clean the data and there is no missing data either, but there is a need for mitigating the imbalance in the labels either by over-sampling or by undersampling. SMOTE (Synthetic Minority Oversampling TEchnique) is used to oversample the data. The data is also standardized before feeding it to the model for training and testing

### Hyper-parameter Tuning

Bayesian Search is employed instead of Grid Search to find the best parameters. And a 3-fold cross validation is used to evaluate the performance.\

Bayesian hyperparameter tuning is a method of optimizing the hyperparameters of a machine learning model by searching for the values that are most likely to lead to good performance. It does this by building a probabilistic model of the hyperparameter space and using techniques from Bayesian statistics to update the model as more data becomes available.


Hyper-parameter space for different models\

_Logistic Regression_\
solver : 'newton-cg, lbfgs\
C : [0.5, 1]\

_SVM_\
kernel : linear, rbf\
C : 0.5, 1\

_AdaBoost_\
n_estimators : 10-50\

_MLP_*\
epochs : 5, 10, 20, 50\
optimizers : adam, rmsprop\

* parameter tuning is done manually for neural networks\

### Results

![samples_bar_chart](https://github.com/saiganeshT/machine-learning/blob/main/miscellaneous/Fraud%20Detection/images/img1.png)

The training data has been over sampled by using Synthetic Minority Oversampling TEchnique (SMOTE) to generate new data for fraudulent transactions. 

Logistic Regression

![logistic_regression_confusion_matrix](https://github.com/saiganeshT/machine-learning/blob/main/miscellaneous/Fraud%20Detection/images/img2.png)

The confusion matrix shows that the logistic regression model is performing well on detecting fraudulent transactions but performing poorly on non-fraudulent ones. This shows that it is overfitting  to the minority class.


SVM

![svm_confusion_matrix](https://github.com/saiganeshT/machine-learning/blob/main/miscellaneous/Fraud%20Detection/images/img3.png)

The confusion matrix shows that the SVM model is performing well on detecting non-fraudulent transactions but performing poorly on fraudulent ones. This shows that it is overfitting to the majority class.


AdaBoost

![adaboost_confusion_matrix](https://github.com/saiganeshT/machine-learning/blob/main/miscellaneous/Fraud%20Detection/images/img4.png)

The confusion matrix shows that the AdaBoost model is performing well on detecting both the classes. This shows that it is generalizing well. This is the best model.

Neural Networks

![architecture](https://github.com/saiganeshT/machine-learning/blob/main/miscellaneous/Fraud%20Detection/images/img8.png)

This figure shows the architecture of our neural network with the number of trainable and non-trainable parameters.

![accuracy_curves](https://github.com/saiganeshT/machine-learning/blob/main/miscellaneous/Fraud%20Detection/images/img5.png)

The accuracy curve on the training data gradually rises with epochs eventually flattening. Whereas the validation curve stays constant. This shows that the model is not overfitting.

![loss_curves](https://github.com/saiganeshT/machine-learning/blob/main/miscellaneous/Fraud%20Detection/images/img6.png)

Interestly, for the loss curves, on training data they are stable whereas they are unstable on validation data.

![neural_network_confusion_matrix](https://github.com/saiganeshT/machine-learning/blob/main/miscellaneous/Fraud%20Detection/images/img7.png)


The confusion matrix shows that the logistic regression model is performing well on detecting fraudulent transactions but performing poorly on non-fraudulent ones. This shows that it is overfitting  to the minority class.

### Lessons Learned
In this project, I discovered that boosting algorithms tend to have better performance when dealing with unbalanced data. I was also introduced to Bayesian hyperparameter search and implemented it for the first time. Additionally, I learned about the weighted f1 score, which is a useful metric for evaluating the performance of algorithms on highly imbalanced data. On the other hand, I found that training support vector machines (SVMs) on a large dataset can be time-consuming.

A key aspect of this project was comparing the performance of various algorithms, including logistic regression, SVM, adaBoost, and neural networks, on imbalanced data, as well as implementing Bayesian hyperparameter search instead of traditional grid search.

One of the challenges I encountered was obtaining precision and recall scores from the neural network, as they consistently came out as zero. After debugging, I discovered that some additional processing was required on the predictions to obtain accurate scores.Overall, this project provides insights into the performance of different algorithms on highly imbalanced data in terms of metrics and time taken.
