### Goal 
To Translate English sentences to French sentences using Neural Machine Translation

### Dataset
The Dataset for French and English sentence pairs are obtained from this [website](https://www.manythings.org/anki/)

### Approach

##### *Data Preprocessing*
1. Drop the unrequired columns from the dataset.
2. Set the number of unique English and French words/tokens to consider.
3. Fit tokenizers on English sentences transform them to numerical sequences.\
    e.g. When he asked who had broken the window, all t...  ---> \[71, 10, 218, 78, 61, 739, 2, 481, 41, 2, 921, 181, 31, 59, 678, 8, 3560] 
5. Add start and end tokens (*SSSS* and *DDDD*) to the French sentences and then fit tokenizers on them.\
    e.g. SSSS Je ne supporte pas ce type. DDDD -----> \[2, 5, 12, 2193, 6, 18, 846, 3] 
6. Set a filter size and remove all the English and corresponding French sentences if it exceeds the threshold set.
    note: *This is done to remove any extremely large sentences and make training easier*
8. Get the new number of tokens and save them for future use.
9. Split the data into training and testing sets.
10. Since the model decoder part expects input French sentences to start with <start> token (i.e SSSS) but not <end> token (i.e. DDDD), remove it from the input of decoder.
11. Similarly, the decoder output outputs sequences without <start> token, remove it.
     Therefore, we have:\
        encoder input: english sequences
        decoder input: french sequences without <end> token
        decoder output: french sequences without <start> token
11. Pad all the sequences so that they can be fed to sequence model.
        

##### *Model Architecture*
1. The model follows encoder-decoder architecture.
2. Encoder takes in padded English sequences as input. 
3. It has an embedding layer which is followed by an LSTM layer.
4. The hidden cell states are given as inputs to the cell states of the decoder.
5. It too has an embedding layer followed by LSTM units.
6. Along with the inputs from the encoder it also takes in input from the user (i.e. decoder input specified above)
7. The output predictions will be compared against *decoder output*.
