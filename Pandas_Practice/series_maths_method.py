import pandas as pd
# count() -> doesn't count missing values
# sum(),product()
# mean(),median(),mode(),std(),var()
# min(),max()
# describe()

vk=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\kohli_ipl.csv",index_col="match_no")
vk=vk.squeeze("columns")

print(vk.count())
print(vk.sum())

subs = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\subs.csv")
subs=subs.squeeze("columns")

print(subs.product())
print(subs.mean())
print(subs.median())
print(subs.std())
print(subs.mode())
print(subs.var())
print(subs.min())
print("akkak")


print(vk.max())
print(vk.describe())