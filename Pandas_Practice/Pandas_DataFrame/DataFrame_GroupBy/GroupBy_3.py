import pandas as pd
import numpy as np

# Load dataset
ipl = pd.read_csv(
    r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\deliveries.csv'
)

# -------------------------------
# 1. Top 10 batsmen by total runs
# -------------------------------
print("\nTop 10 batsmen by total runs scored:")
top_batsmen_runs = (
    ipl.groupby('batsman')['batsman_runs']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_batsmen_runs)

# --------------------------------------
# 2. Virat Kohli records against each team
# --------------------------------------
print("\nVirat Kohli runs scored against each team:")
kohli_data = ipl[ipl['batsman'] == 'V Kohli']
kohli_vs_team = (
    kohli_data.groupby('bowling_team')['batsman_runs']
    .sum()
    .sort_values(ascending=False)
)
print(kohli_vs_team)

# ---------------------------------
# 3. Batsman with most sixes overall
# ---------------------------------
print("\nBatsman with the maximum number of sixes:")
sixes_data = ipl[ipl['batsman_runs'] == 6]
most_sixes = (sixes_data.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1)
)
print(most_sixes)

# --------------------------------------------------
# 4. Most 4s and 6s in the last 5 overs (16th - 20th)
# --------------------------------------------------
print("\nBatsman with most 4s and 6s in last 5 overs:")
death_overs = ipl[ipl['over'] > 15]
boundary_data = death_overs[(death_overs['batsman_runs'] == 4) | (death_overs['batsman_runs'] == 6)]

# Total runs from 4s and 6s
top_boundary_batsman = (boundary_data.groupby('batsman')['batsman_runs'] .sum().sort_values(ascending=False).head(1))
print(top_boundary_batsman)

# Split into 4s and 6s counts separately
boundary_counts = (boundary_data.groupby('batsman_runs')['batsman'] .value_counts().reset_index(name='count'))

fours_leader = (boundary_counts[boundary_counts['batsman_runs'] == 4].sort_values('count', ascending=False).reset_index(drop=True))

sixes_leader = (boundary_counts[boundary_counts['batsman_runs'] == 6].sort_values('count', ascending=False).reset_index(drop=True))

print("\nBoundary counts (raw data):")
print(boundary_counts)

print("\nTop batsmen by 4s in death overs:")
print(fours_leader)

print("\nTop batsmen by 6s in death overs:")
print(sixes_leader)

# -------------------------------------------------------
# 5. Function: Highest score by a batsman in single match
# -------------------------------------------------------
def highest_score(batsman_name):
    """Return the top 5 highest scores of a batsman across matches."""
    batsman_data = ipl[ipl['batsman'] == batsman_name]
    top_scores = (batsman_data.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(5))
    print(f"\nTop 5 scores for {batsman_name}:")
    print(top_scores)


# Ask user for batsman name
batsman_input = input("\nEnter the batsman name: ")
highest_score(batsman_input)
