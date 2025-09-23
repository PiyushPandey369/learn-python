import numpy as np
import matplotlib.pyplot as plt

# Dictionary mapping candidate IDs to their names
candidate_dict = {
    0: 'Nepali Congress',
    1: 'Rastriya Sotantra Party',
    2: 'Rastriya Prajatantra Party',
    3: 'Sotantra Yuva',
    4: 'GenZ Nepali',
    5: 'Aam Aadmi Party'
}

# Votes matrix: regions x candidates x [male, female]
votes_matrix = np.array([
    [
        [500, 50], [700, 300], [600, 300], [57, 80], [1230, 210], [157, 110]  # Region 1
    ],
    [
        [90, 60], [400, 600], [750, 250], [900, 160], [200, 180], [140, 160]  # Region 2
    ],
    [
        [1200, 800], [400, 600], [50, 40], [70, 20], [150, 216], [130, 140]    # Region 3
    ]
])

# Function to calculate seat allocation
def seat_calculation(vote_by_party, winner_list):
    total_seats_votes = 120   # Seats from proportional votes
    bonus_per_region = 10     # Bonus seats per regional winner

    # Step 1: Calculate proportional seats from votes
    seats_from_votes = [round(v / 100) for v in vote_by_party]

    # Step 2: Add bonus seats for regional winners
    for winner in winner_list:
        seats_from_votes[winner] += bonus_per_region

    # Step 3: Display final seat allocation
    print("\n----------- Seat Allocation -----------")
    for idx, name in enumerate(candidate_dict.values()):
        print(f"{name}: Votes = {vote_by_party[idx]}, Total Seats = {seats_from_votes[idx]}")

# Track overall winners
winner_list = []
vote_by_party = []
max_vote = 0
max_vote_party = ""

print("----------- Election Result -----------\n")

# Calculate and display results for each region
for region_index in range(3):
    print(f"--------- Result of Region {region_index + 1} ---------")
    total_region_votes = np.sum(votes_matrix[region_index])
    total_male_votes = np.sum(votes_matrix[region_index, :, 0])
    total_female_votes = np.sum(votes_matrix[region_index, :, 1])

    print(f"Total voters: {total_region_votes}")
    print(f"Total male voters: {total_male_votes}")
    print(f"Total female voters: {total_female_votes}\n")

    for candidate_index in range(6):
        candidate_votes = np.sum(votes_matrix[region_index, candidate_index])
        male_votes = votes_matrix[region_index, candidate_index, 0]
        female_votes = votes_matrix[region_index, candidate_index, 1]
        print(f"{candidate_dict[candidate_index]} : {candidate_votes} (Male: {male_votes}, Female: {female_votes})")

    # Regional winner
    winner_region = np.argmax(np.sum(votes_matrix[region_index], axis=1))
    print(f"\nWinner from Region {region_index + 1}: {candidate_dict[winner_region]}\n")
    winner_list.append(winner_region)

# Calculate total votes per candidate across all regions
for candidate_index in range(6):
    total_votes_candidate = np.sum(votes_matrix[:, candidate_index])
    total_male = np.sum(votes_matrix[:, candidate_index, 0])
    total_female = np.sum(votes_matrix[:, candidate_index, 1])

    vote_by_party.append(total_votes_candidate)

    print(f"{candidate_dict[candidate_index]} : {total_votes_candidate}")
    print(f"{candidate_dict[candidate_index]} male voters: {total_male}")
    print(f"{candidate_dict[candidate_index]} female voters: {total_female}\n")

    if total_votes_candidate > max_vote:
        max_vote = total_votes_candidate
        max_vote_party = candidate_dict[candidate_index]

# Overall election summary
total_votes = np.sum(votes_matrix)
total_male_votes = np.sum(votes_matrix[:, :, 0])
total_female_votes = np.sum(votes_matrix[:, :, 1])

print("----------- Overall Result -----------")
print(f"Total voters: {total_votes}")
print(f"Total male voters: {total_male_votes}")
print(f"Total female voters: {total_female_votes}")
print(f"Overall maximum vote gained by {max_vote_party}: {max_vote}")

# Seat allocation
seat_calculation(vote_by_party, winner_list)


# vote_by_party contains total votes per candidate
vote_by_party_array = np.array(vote_by_party)

'''
# Define bins (for example: 0-500, 501-1000, 1001-1500, ...)
bins = [0, 500, 1000, 1500, 2000, 2500, 3000]

hist, bin_edges = np.histogram(vote_by_party_array, bins=bins)

print("Histogram counts:", hist)
print("Bin edges:", bin_edges)

candidate_names = list(candidate_dict.values())

plt.figure(figsize=(12, 6))
plt.bar(candidate_names, vote_by_party, color='skyblue')
plt.xlabel("Candidates")
plt.ylabel("Total Votes")
plt.title("Total Votes per Candidate")
plt.xticks(rotation=10)  # Rotate names 
plt.show()
'''
