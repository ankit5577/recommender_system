import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings) 

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

corrMatrix = userRatings.corr(method='pearson', min_periods=100)

myRatings = userRatings.iloc[1].dropna()

myratingnew = myRatings[1:50]

simCandidates = pd.Series()
for i in range(0, len(myratingnew.index)):
    print ("Adding sims for " + myratingnew.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myratingnew.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myratingnew[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
print (simCandidates.head(10))


filteredSims = simCandidates.drop(myRatings.index)
filteredSims.head(10)
