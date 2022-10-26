### Goal
To build a simple recommendation system using collaborative filtering

### Approach
1. Calculate similarity between users.
2. Rate the unseen movies by the current user with the help of other user’s ratings and their similarity with the current user.\
	    *predicted rating = similarity(current user, other user) * ( user’s rating)*
3. Sum such predicted ratings and normalized them to get the final predicted rating\
	    *Final Predicted Rating = sum(scores)/ count(scores)*
4. Finally, predict the top n movies with highest scores

### Similarity Measures
1. L2 Distance 
2. Pearson’s Correlation

