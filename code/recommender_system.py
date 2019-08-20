import pandas as pd
import numpy as np

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

# ploting table for movie rating
movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

# getting ratings for Star wars by all users
starWarsRatings = movieRatings['Star Wars (1977)']

# pandas inbuilt correlation function
similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)

# similarMovies.sort_values(ascending=False)
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})

# get rid of suggestions rated by less than 100 peoples
popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))

df.sort_values(['similarity'], ascending=False)[:15]







