import pandas as pd

# matches=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\matches.csv'
# courses=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\bollywood.csv'
# nov=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv'
# dec=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month2.csv'
# students=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv'
nov=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv')
dec=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month2.csv')
# Display November data
print("November Data")
print(nov)

# Display December data
print("December Data")
print(dec)

# Concatenate vertically (default) -> Index values will be repeated
print("After concatenating (Index will be repeated)")
c = pd.concat([nov, dec])
print(c)

# Concatenate vertically but reset index -> New continuous index is created
print("Indexing resolved (ignore_index=True):")
print(pd.concat([nov, dec], ignore_index=True))

# Concatenate horizontally (side by side, column-wise)
print("Horizontally concatenated Data:")
d = pd.concat([nov, dec], axis=1)
print(d)

# MultiIndex concatenation with keys -> Helps to differentiate Nov and Dec data
print("MultiIndex Concatenation:")
m = pd.concat([nov, dec], keys=['Nov', 'Dec'])
print(m)

# Access December data using the key 'Dec'
print("Accessing December Data using MultiIndex:")
print(m.loc['Dec'])

# Access a single row from November data -> ('Nov', 0) means November, row with index 0
print("Accessing single row from November (row 0):")
print(m.loc[('Nov', 0)])

