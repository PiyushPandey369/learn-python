import pandas as pd
# Adding new cols
student_dict = {
    'iq': [100, 120, 90],
    'marks': [89, 79, 67],
    'package': [12, 8, 4]
}

student = pd.DataFrame(student_dict)
print(student)
student['Gender']='Male'
print(student)

movie = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\movies.csv')
movie.dropna(inplace=True)
movie['lead_actor']=movie['actors'].str.split('|').apply(lambda x:x[0])
print(movie.head())