import pandas as pd
import numpy as np


movies=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\imdb-top-1000.csv')
print(movies.head(3))
# Find the director who made highest number of movies
print(movies.groupby('Director')['Series_Title'].count().sort_values(ascending=False))
# Find the top 3 genres by total earning
print(movies.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3))
# Find the highest gross movie
print(movies.groupby('Series_Title')['Gross'].sum().sort_values(ascending=False).head(1))
# find the genre with highest average IMDB rating
print(movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1))
# find the director with most popularity
print(movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1))
# find the number of movies done by each actor
print(movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False).head(5))


