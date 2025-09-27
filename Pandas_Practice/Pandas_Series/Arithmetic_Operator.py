import pandas as pd
import matplotlib.pyplot as plt

marks=[70,46,90,78]
subjects=["Physic","English","Maths","Computer"]
marks_series=pd.Series(marks,index=subjects)
print(marks_series)

print(100-marks_series)
print(100+marks_series)
print(100*marks_series)
print(100/marks_series)
print(100%marks_series)


# Relational Operators
vk=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\kohli_ipl.csv",index_col="match_no").squeeze("columns")
# print(vk[vk>=50])
# find the numbers of ducks
print(vk[vk==0].size)


movies=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\bollywood.csv",index_col="movie").squeeze("columns")
movies_values=movies.value_counts()
c=movies_values[movies_values>20]
print(c)

# c.plot(kind="pie")
vk.plot()


plt.show()