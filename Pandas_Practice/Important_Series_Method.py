import pandas as pd
import sys
import numpy as np
vk=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\kohli_ipl.csv",index_col="match_no").squeeze("columns")
# print(sys.getsizeof(vk))
subs=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\subs.csv").squeeze("columns")
# print(sys.getsizeof(vk.astype('int8')))

# print(subs.clip(100,200))

temp=pd.Series([11,23,43,56,77,11,23,77,89])
print(temp)
print(temp.drop_duplicates())

# Missing Values
temp=pd.Series([11,np.nan,43,56,np.nan,11,23,77,np.nan,11,10])
print(temp.isnull().sum())

# remove missing value
print(temp.dropna())

print(temp.fillna(0))

print(vk[vk.isin([99,49])])
# apply() -> helps to apply custom logic
print(vk.apply(lambda x:'Good day' if x>49 else 'Bad Day'))

