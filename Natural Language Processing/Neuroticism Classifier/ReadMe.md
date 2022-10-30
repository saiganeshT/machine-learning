### Goal
To classify whether an individual is neurotic or not

### Dataset
The dataset contains users' social media posts and their corresponding personality traits manually labeled.\
**This is a private dataset** so it couldn't be provided in the GitHub repository.

### Approaches

1. #### Logistic Regression on Bag of Words

#### *Data Pre-Processing*
1. Read the csv files and extract text and lables.
2. Convert text to tokens using Spacy tokenizer.
3. Extract bigrams and unigrams from the tokenzied text.
4. Remove the n-grams that contain stopwords and any punctuation.
5. Combine all the n-grams into a feature string.
6. Process the feature string by inputting to the CountVectorizer function in scikit-learn library.
7. Split the data into training and testing sets.
8. Pass training set as input to logistic regression model

**_Note: other personality traits are not used as input in this model_**

2. #### Neural Networks
    
#### *Data Pre-Processing*
1. Convert the 'yes' or 'no' labels of personality traits to numerical features as 1 and 0.
2. Tokenize the text using a tokenizer and pad them accordingly.
3. Split them into training and testing sets.
    
#### a. Custom Model
1. In this version of the model, all the layers are trained from scratch starting with embedding layer and followed by LSTM, Dropout and BatchNormalization layers.
2. The above component of the model is used to process text.
3. After repeating such blocks for 2-3 times, the output is concatenated with the input from categrical variables (personlity traits).
4. This is passed through dense and normalization layers before passing it to the final classification layer.

#### b. Transfer Learning
1. Instead of training word embeddings from scratch an embedding layer form tensorflow hub is used.
2. This spits out vectors for every sentence in the training dataset which are sent through dense and dropout layers before concatenating with categroical data.
3. Rest of the architecture is similar to the above model.


### Performance
The transfer learning model did better than the custom trained model both in the terms of training time and accuracy metrics.
