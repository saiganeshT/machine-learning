
#### Goal
To predict genre of a given song

#### Dataset
[MagnaTagATune](https://mirg.city.ac.uk/codeapps/the-magnatagatune-dataset)

#### Approach
###### *Data Preprocessing* ######
1. Found all the genres that are similar and made a list. \
e.g. \['electro', 'electronic', 'electronica', 'electric']
2. Condensed all such genres and named them with the first in the list.\
e.g. 'electro' or 'electronic' or 'electric' will all be named 'electric'
3. Renamed all the *mp3* files with their corresponding *clip id* from the annotations, so that X (mp3 files) and y (annotations) are mapped easily.
4. Converted all the audio files to mel-spectograms and saved them as numpy arrays.\
note: **this is a compute intensive operation**
5. Dropped all the audio files that failed to convert.

###### *Model Training* ######
1. As the batched mel-spectograms are huge in size (~ 1GB), built a generator to feed them one by one so that it doesn't break the computer.
2. Trained several different models (such as ConvNets, LSTMs, GRUs) and their chimeras to find the best model.
3. Plotted all the curves and performance metrics such as training time and accuracy are notted.
