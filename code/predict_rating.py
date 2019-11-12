import pandas as pd
import numpy as np
from scipy import spatial
import operator

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))

# grouping movie by id and np.size is total no. of ratings and mean is average
movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})   

# normalizing dataset within range {range is most popular and least popular}
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

movieDict = {}
with open(r'ml-100k/u.item') as f:
    temp = ''
    for line in f:
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))
        
# movieDict[2] or movieDict[Index] will give an array where 0: will be title, 1:will be array for genre where 0 means false 1 means movie was of this genre type, 2: will be popularity score, 3: will be average rating
def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance

# computeDistance will give difference in movies genre or how difference they are from each other

# computing distance for movie2, movie4 just to see it working
ComputeDistance(movieDict[2], movieDict[4])

def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors

# K will give nearest neighbours (Movies)
K = 10
avgRating = 0

# we are using 1 as a dummy and this will return us similar movies upto 10 as K is 10 and avgRating will store predicted average rating.
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))
    
avgRating /= float(K)
# now avgRating will give rating of 10 nearest neighbour to movieDict[1]
avgRating
movieDict[1]
# by using only movieDict[1] this will give you average rating from true dataset, rest you can calculate the difference between pridicted value and original value.






