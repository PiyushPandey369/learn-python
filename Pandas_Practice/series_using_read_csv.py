
# csv -> Comma Separated values
# read_csv -> import csv file
# pd.read_csv takes argument like: path, squeeze

import pandas as pd

# Read CSV with one column → directly as Series
subs = pd.read_csv(
    r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\subs.csv"
)
subs=subs.squeeze("columns")
print(type(subs))
print(subs)

# Read CSV with two column → directly as Series
vk=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\kohli_ipl.csv",index_col="match_no")
vk=vk.squeeze("columns")
print(vk)

movies=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\bollywood.csv",index_col="lead")
movies=movies.squeeze("columns")
print(movies)