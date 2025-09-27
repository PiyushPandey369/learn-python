import pandas as pd

# len/type/dir/sorted/max/min

subs = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\subs.csv").squeeze("columns")

# print(len(subs))
# print(type(subs))
# print(dir(subs))
# print(sorted(subs))
# print(min(subs))
# print(max(subs))

# type conversion
runs=[3,67,5,33,80,110,0,145]
runs_series=pd.Series(runs)
print(type(runs_series))
print(type(list(runs_series)))

# membership operator
print(184 in subs) # -> search in index

movies=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\bollywood.csv",index_col="lead").squeeze("columns")

print("Emraan Hashmi" in movies) # -> search in index
print("Kaante" in movies.values) # -> search in value

# for i in movies.values:
#     print(i)
# for i in movies.index:
#     print(i)
