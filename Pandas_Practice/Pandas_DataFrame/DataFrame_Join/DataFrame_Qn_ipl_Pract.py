import pandas as pd
import numpy as np

matches=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\matches.csv')
ipl_deliver=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\deliveries.csv")


# print(matches)

# print(ipl_deliver)


# 1) Find orange cap holder of each season
team_df=matches.merge(ipl_deliver,how='inner',left_on='id',right_on='match_id')
orange_cap=team_df.groupby(['season','batsman'])['batsman_runs'].sum().reset_index().sort_values(by='batsman_runs',ascending=False).drop_duplicates(subset=['season']).sort_values('season')
print(orange_cap)

