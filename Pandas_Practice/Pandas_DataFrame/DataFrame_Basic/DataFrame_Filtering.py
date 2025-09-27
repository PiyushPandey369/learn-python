import pandas as pd

# -----------------------------
# Load CSV files
# -----------------------------
ipl = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\ipl-matches.csv')
movie = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\movies.csv')

# Filtering DataFrame

# Q1)Find all IPL final winner

ipl_final=ipl[ipl['MatchNumber']=='Final']
print(ipl_final[['Season','WinningTeam']])

#  Q2)How many super over finished have occured
ipl_super_over=ipl[ipl['SuperOver']=='Y'].shape[0]
print(ipl_super_over)

#  Q3)How many matches has CSK won in Kolkata
ipl_CSK_records=ipl[(ipl['City']=='Kolkata') & (ipl['WinningTeam']=='Chennai Super Kings')].shape[0]
print(ipl_CSK_records)

#  Q4)Toss Winner is match winner in percentage
ipl_toss_records=(ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0])/ipl.shape[0]*100
print(ipl_toss_records)

#  Q4)Write a function that can track record of 2 teams against each other
def fxn_check(team1,team2):
    ipl_records = ipl[
        ((ipl['Team1'] == team1) & (ipl['Team2'] == team2)) |
        ((ipl['Team1'] == team2) & (ipl['Team2'] == team1))
    ]
    
    # Handle empty data
    if ipl_records.empty:
        print(f"No matches found between {team1} and {team2}.")
        return
    
    # Count wins
    a_won = (ipl_records['WinningTeam'] == team1).sum()
    b_won = (ipl_records['WinningTeam'] == team2).sum()
    draw = len(ipl_records) - a_won - b_won  # remaining matches are draws or no result

    print(f"Total matches: {len(ipl_records)}")
    print(f"{team1} wins: {a_won}")
    print(f"{team2} wins: {b_won}")
    print(f"Draw/No Result: {draw}")

fxn_check('Rajasthan Royals', 'Royal Challengers Bangalore')

#  Q5) movies with rating higher than 8 and votes > 10000
movie_imdb_records=movie[(movie['imdb_rating'] > 8 )& (movie['imdb_votes'] > 10000)].shape[0]
print(movie_imdb_records)
# Action movies with rating higher than 7.5
a=movie['genres'].str.contains("Action")
b=movie['imdb_rating'] > 7.5
print(movie[a & b])

# Q6) Find which player has won most potm -> finals and qualifier
ipl_ptm_records=ipl[(ipl['MatchNumber']=='Final') | ipl['MatchNumber'].isin(["Qualifier", "Qualifier 1", "Qualifier 2"])]
ipl_ptm_name=ipl_ptm_records['Player_of_Match'].value_counts().index[0]
ipl_ptm_max=ipl_ptm_records['Player_of_Match'].value_counts().iloc[0]

print(ipl_ptm_name,ipl_ptm_max)

# Q7) How many matches each team has played
ipl_team=ipl['Team1'].value_counts() + ipl['Team2'].value_counts()
print(ipl_team)
