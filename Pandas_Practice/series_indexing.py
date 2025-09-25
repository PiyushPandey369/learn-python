import pandas as pd

x=pd.Series([1,2,3,4,5,6,7,8,9,11,23,66])
print(x[1])  # -> 2
# print(x[-1])   -> error

movies=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\bollywood.csv",index_col="movie").squeeze("columns")
print(movies[6])
print(movies[-1])
# If we use series[some_int] and that integer is not an index label, Pandas treats it as a position.
# That’s why movies[6] gave the 7th row (positional lookup).
# Similarly, movies[-1] gave the last row.

'''
Correct Way:
# By position
print(movies.iloc[6])   # 7th row
print(movies.iloc[-1])  # last row

# By label (movie name as index)
print(movies.loc['Fraud Saiyaan'])
'''
print(movies['Fraud Saiyaan'])



vk=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\kohli_ipl.csv",index_col="match_no").squeeze("columns")
print(vk[105:111]) # -> slicing
print(vk[[9,11,89,3]]) # -> fancy indexing
print(vk[(vk.values>49) & (vk.values<100)].size) # -> Boolean Indexing

