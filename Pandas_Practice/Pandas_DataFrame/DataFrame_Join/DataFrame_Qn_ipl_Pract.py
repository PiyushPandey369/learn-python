import pandas as pd
import numpy as np

# Load the datasets
matches = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\matches.csv')
deliveries = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\deliveries.csv")

# Merge matches and deliveries dataset
team_df = matches.merge(deliveries, how='inner', left_on='id', right_on='match_id')

# ------------------------------
# 1) Death Overs Analysis (Overs 16–20)
# ------------------------------
death_over_df = team_df[team_df['over'] > 15]

# Filter out run-outs and NA dismissals for wicket calculation
death_over_wic = death_over_df[
    ~((death_over_df['dismissal_kind'] == 'run out') | (death_over_df['dismissal_kind'].isna()))
]

# Count wickets in death overs per bowler
death_wickets = (
    death_over_wic.groupby('bowler')['dismissal_kind']
    .count()
    .reset_index()
    .sort_values(by='dismissal_kind', ascending=False)
    .rename(columns={'dismissal_kind': 'Wickets'})
)

print("Highest Wickets in Death Overs:")
print(death_wickets)

# ------------------------------
# 2) Economy Calculation in Death Overs
# ------------------------------
# Runs conceded in death overs
death_runs = (
    death_over_df.groupby('bowler')['total_runs']
    .sum()
    .reset_index()
)

# Balls bowled in death overs
death_balls = (
    death_over_df.groupby('bowler')['ball']
    .count()
    .reset_index()
)

# Convert balls → overs
death_balls['overs'] = death_balls['ball'] / 6

# Merge runs + overs
economy_df = death_balls.merge(death_runs, how='inner', on='bowler').drop(columns=['ball'])

# Economy rate = runs / overs
economy_df['economy'] = economy_df['total_runs'] / economy_df['overs']

# Merge economy data with wicket data
economy_df = (
    economy_df.merge(death_wickets, how='inner', on='bowler')
    .sort_values(by='Wickets', ascending=False)
)

print("\nDeath Overs Bowling Performance (Wickets + Economy):")
print(economy_df)

# ------------------------------
# 3) Extra Analysis (Orange & Purple Cap)
# ------------------------------

# # Find Orange Cap holder of each season
orange_cap = (
    team_df.groupby(['season', 'batsman'])['batsman_runs']
    .sum()
    .reset_index()
    .sort_values(by='batsman_runs', ascending=False)
    .drop_duplicates(subset=['season'])
    .sort_values('season')
)
print(orange_cap)

# # Find Purple Cap holder of each season
team_df_bowl = team_df[
    ~((team_df['dismissal_kind'] == 'run out') | (team_df['dismissal_kind'].isna()))
]
purple_cap = (
    team_df_bowl.groupby(['season', 'bowler'])['dismissal_kind']
    .count()
    .reset_index()
    .sort_values(by='dismissal_kind', ascending=False)
    .drop_duplicates(subset=['season'], keep='first')
    .sort_values(by='season')
    .rename(columns={'dismissal_kind': 'Wicket_Taken'})
)
print(purple_cap)


