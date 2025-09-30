import pandas as pd
import numpy as np

movies=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\imdb-top-1000.csv')

genres=movies.groupby('Genre')
a=genres.agg({
    'Runtime':'mean',
    'IMDB_Rating':'mean',
    'Gross':'sum'
})
print(movies.columns.tolist())

print(a)
b = genres[['IMDB_Rating', 'Metascore']].agg(['mean', 'min', 'max'])
print(b)



