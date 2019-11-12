import pandas as pd

ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id', 'movie_id', 'rating'], usecols=range(3), encoding="ISO-8859-1")
movies = pd.read_csv('ml-100k/u.item', sep='|', names=['movie_id', 'title'], usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

# dataset tweak
allRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

# you can use pearson or spearman method for calculation too
corrMatrix = allRatings.corr(method='pearson', min_periods=100)

# taking frst user as fakeuser and droping NA values
fakeUser = allRatings.iloc[1].dropna()

# taking user's first 50 ratings
fakeUserRatings = fakeUser[1:50]

simCandidates = pd.Series()
for i in range(0, len(fakeUserRatings.index)):
    # getting similar movies
    sims = corrMatrix[fakeUserRatings.index[i]].dropna()
    # scaling similarity by how fake_user rated this movie
    sims = sims.map(lambda x: x * fakeUserRatings[i])
    # Adding score to list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
# removing watched movies not working 
## filteredSims = simCandidates.drop(fakeUser.index)
simCandidates.sort_values(inplace = True, ascending = False)
# top 20 recommended movies should be -
simCandidates.head(20)
