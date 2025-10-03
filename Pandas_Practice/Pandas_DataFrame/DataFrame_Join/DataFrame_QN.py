import pandas as pd
import numpy as np

# Load the datasets
matches = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\matches.csv')
deliveries = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\deliveries.csv")

# Merge matches and deliveries dataset
# ['Season','Innings', 'TotalRuns', 'Avg', 'HighestScore','StrikeRate'].

team_df = matches.merge(deliveries, how='inner', left_on='id', right_on='match_id')


# Filter Warner
warner_df = team_df[team_df['batsman']=='DA Warner']

# Total runs per season
total_runs = warner_df.groupby('season')['batsman_runs'].sum()

# Balls faced per season
balls = warner_df.groupby('season')['ball'].count()

# Innings (unique matches batted)
innings = warner_df.groupby('season')['match_id'].nunique()

# Strike rate
strike_rate = (total_runs / balls) * 100

# Highest score per season
highest_score = warner_df.groupby(['season','match_id'])['batsman_runs'].sum().groupby('season').max()

# Combine into one DataFrame
warner_stats = pd.concat(
    [total_runs, balls, innings, strike_rate, highest_score], 
    axis=1
)

warner_stats.columns = ['TotalRuns','BallsFaced','Innings','StrikeRate','HighestScore']

print(warner_stats)
