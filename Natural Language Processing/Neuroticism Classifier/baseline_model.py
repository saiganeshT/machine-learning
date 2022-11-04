# imports
import csv
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import csv, re
import string
from tqdm import tqdm
import codecs
from collections import Counter
from spacy.lang.en import English

# Hard-wired variables
input_speechfile   = "./wcpr_mypersonality.csv"
stopwords_file     = "./mallet_en_stoplist.txt"


# FUNCTIONS
def read_and_clean_lines(infile):
    print("\nReading and cleaning text from {}".format(infile))
    lines = []
    neurotic_flags = []

    with open(infile, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            lines.append(row[1])
            neurotic_flags.append(row[8])

    print("Read {} status posts.".format(len(lines)))
    print("Read {} labels".format(len(neurotic_flags)))
    return lines, neurotic_flags

# Read a set of stoplist words from filename, assuming it contains one word per line
def load_stopwords(filename):
    stopwords = []
    with codecs.open(filename, 'r', encoding='ascii', errors='ignore') as fp:
        stopwords = fp.read().split('\n')
    return set(stopwords)


# Call sklearn's train_test_split function to split the dataset into training items/labels

def split_training_set(lines, labels, test_size=0.2, random_seed=42):
    X_train, X_test, y_train, y_test = train_test_split(lines, labels, test_size=test_size, shuffle=False)
    print("Training set label counts: {}".format(Counter(y_train)))
    print("Test set     label counts: {}".format(Counter(y_test)))
    return X_train, X_test, y_train, y_test

# Converting text into features.

def convert_text_into_features(X, stopwords_arg, analyzefn="word", range=(1,2)):
    training_vectorizer = CountVectorizer(stop_words=stopwords_arg,
                                          analyzer=analyzefn,
                                          lowercase=True,
                                          ngram_range=range)
    X_features = training_vectorizer.fit_transform(X)
    return X_features, training_vectorizer

# Input:
#    lines     - a raw text corpus, where each element in the list is a string
#    stopwords - a set of strings that are stopwords
#    remove_stopword_bigrams = True or False

def convert_lines_to_feature_strings(lines, stopwords, remove_stopword_bigrams=True):

    print(" Converting from raw text to unigram and bigram features")
    if remove_stopword_bigrams:
        print(" Includes filtering stopword bigrams")
        
    print(" Initializing")
    nlp          = English(parser=False)
    all_features = []
    print(" Iterating through documents extracting unigram and bigram features")
    for line in tqdm(lines):
        
        # Get spacy tokenization and normalize the tokens
        spacy_analysis    = nlp(line)
        spacy_tokens      = [token.orth_ for token in spacy_analysis]
        normalized_tokens = normalize_tokens(spacy_tokens)

        # Collect unigram tokens as features
        # Exclude unigrams that are stopwords or are punctuation strings (e.g. '.' or ',')
        unigrams          = [token   for token in normalized_tokens
                                 if token not in stopwords and token not in string.punctuation]

        # Collect string bigram tokens as features
        bigrams = []
        bigram_tokens     = ["_".join(bigram) for bigram in bigrams]
        bigrams           = ngrams(normalized_tokens, 2) 
        bigrams           = filter_punctuation_bigrams(bigrams)
        if remove_stopword_bigrams:
            bigrams = filter_stopword_bigrams(bigrams, stopwords)
        bigram_tokens = ["_".join(bigram) for bigram in bigrams]

        # Conjoin the feature lists and turn into a space-separated string of features.

        # feature_string = []
        feature_string = " ".join(unigrams) + " " + " ".join(bigram_tokens)

        # Add this feature string to the output
        all_features.append(feature_string)

        
    return all_features

# Split on whitespace, e.g. "a    b_c  d" returns tokens ['a','b_c','d']
def whitespace_tokenizer(line):
    return line.split()

def normalize_tokens(tokenlist):
    # Input: list of tokens as strings,  e.g. ['I', ' ', 'saw', ' ', '@psresnik', ' ', 'on', ' ','Twitter']
    # Output: list of tokens where
    normalized_tokens = [token.lower().replace('_','+') for token in tokenlist   # lowercase, _ => +
                             if re.search('[^\s]', token) is not None            # ignore whitespace tokens
                             and not token.startswith("@")                       # ignore  handles
                        ]
    return normalized_tokens        

# Take a list of string tokens and return all ngrams of length n,
def ngrams(tokens, n):
    # Returns all ngrams of size n in sentence, where an ngram is itself a list of tokens
    return [tokens[i:i+n] for i in range(len(tokens)-n+1)]

def filter_punctuation_bigrams(ngrams):
    # Input: assume ngrams is a list of ['token1','token2'] bigrams
    # Removes ngrams like ['today','.'] where either token is a punctuation character
    # Returns list with the items that were not removed
    punct = string.punctuation
    return [ngram   for ngram in ngrams   if ngram[0] not in punct and ngram[1] not in punct]

def filter_stopword_bigrams(ngrams, stopwords):
    result = [ngram   for ngram in ngrams   if ngram[0] not in stopwords and ngram[1] not in stopwords]
    return result
        

def main():
    # Get stop words in a list
    stop_words = load_stopwords(stopwords_file)

    # Read the dataset in and split it into training documents/labels (X) and test documents/labels (y)
    X_train, X_test, y_train, y_test = split_training_set(*read_and_clean_lines(input_speechfile))
    
    # Call convert_lines_to_feature_strings() to get your features
    print("Creating feature strings for training data")
    X_train_feature_strings = convert_lines_to_feature_strings(X_train, stop_words)
    print("Creating feature strings for test data")
    X_test_documents        = convert_lines_to_feature_strings(X_test,  stop_words)
    
    X_features_train, training_vectorizer = convert_text_into_features(X_train_feature_strings, stop_words, whitespace_tokenizer)
        
    # Create a logistic regression classifier trained on the featurized training data
    lr_classifier = LogisticRegression(solver='liblinear')
    lr_classifier.fit(X_features_train, y_train)

    # Apply the "vectorizer" created using the training data to the test documents, to create testset feature vectors
    X_test_features =  training_vectorizer.transform(X_test_documents)

    # Classify the test data
    print("Classifying test data...")
    predicted_labels = lr_classifier.predict(X_test_features)
    print('Accuracy  = {}'.format(metrics.accuracy_score(predicted_labels,  y_test)))
    for label in ['n', 'y']:
        print('Precision for label {} = {}'.format(label, metrics.precision_score(predicted_labels, y_test, pos_label=label)))
        print('Recall    for label {} = {}'.format(label, metrics.recall_score(predicted_labels,    y_test, pos_label=label)))
    
    # Graph the confusion matrix to show accuracies
    print("Generating plots...")
    metrics.plot_confusion_matrix(lr_classifier, X_test_features, y_test, normalize='true')
    plt.show()


if __name__ == "__main__":
    main()

