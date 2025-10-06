import pandas as pd

# Load dataset
ipl = pd.read_csv(
    r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\deliveries.csv"
)

# Filter caught dismissals
catch_record = ipl[ipl["dismissal_kind"] == "caught"]

# Filter "obstructing the field" dismissals
obs_record = ipl[ipl["dismissal_kind"] == "obstructing the field"]

# Create batting partnerships (unordered)
ipl["pair"] = ipl.apply(lambda row: tuple(sorted([row["batsman"], row["non_striker"]])),axis=1)

# Calculate total runs for each partnership
partnership = ( ipl.groupby("pair")["total_runs"].sum().sort_values(ascending=False))


# -------------------------------------------
# Function: Head-to-head stats (batsman vs bowler)
# -------------------------------------------
def players(batsman: str, bowler: str) -> None:
    """Show batting records of a batsman against a specific bowler."""
    records = ipl[(ipl["batsman"] == batsman) & (ipl["bowler"] == bowler)]

    total_runs = records["batsman_runs"].sum()
    run_distribution = records["batsman_runs"].value_counts()
    dismissals = records["player_dismissed"].value_counts()
    dismissal_types = records["dismissal_kind"].value_counts()

    print(f"\n Head-to-Head: {batsman} vs {bowler}")
    print("-" * 40)
    print(f" Total Runs Scored: {total_runs}")
    print("\n Run Distribution (per ball):")
    print(run_distribution.to_string())
    print("\n Dismissals:")
    print(dismissals.to_string())
    print("\n Dismissal Types:")
    print(dismissal_types.to_string())
    print("-" * 40)


# Example usage
players("SK Raina", "SP Narine")
