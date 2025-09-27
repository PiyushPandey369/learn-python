import pandas as pd

s=pd.Series([10,12,13,14,90,100])
print(s)
s_view = s[1:4]  
s_view[0] = 99
print(s)