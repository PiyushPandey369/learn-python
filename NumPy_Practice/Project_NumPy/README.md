
# Election Data Analysis System

A comprehensive Python-based election analysis system that processes and visualizes voting data across multiple regions and candidates, providing detailed insights into election results.

## 📊 Overview

This system analyzes election data by:
- Processing votes across multiple regions and candidates
- Calculating gender-wise vote distributions
- Determining regional winners and overall results
- Allocating parliamentary seats based on proportional representation and bonus seats
- Providing comprehensive statistical analysis and visualization

## 🏛️ Political Parties

The system tracks the following political parties:

| ID | Party Name |
|----|------------|
| 0 | Nepali Congress |
| 1 | Rastriya Sotantra Party |
| 2 | Rastriya Prajatantra Party |
| 3 | Sotantra Yuva |
| 4 | GenZ Nepali |
| 5 | Aam Aadmi Party |

## 🗳️ Data Structure

The voting data is organized in a 3D matrix:

- **Dimensions**: 3 regions × 6 candidates × 2 gender categories
- **Gender Categories**: [Male, Female]
- **Regions**: Region 1, Region 2, Region 3

## ⚙️ Features

### 1. Regional Analysis
- Total votes per region
- Gender-wise vote distribution
- Regional winner determination
- Detailed candidate performance by region

### 2. Overall Election Results
- Total votes across all regions
- Gender-wise overall statistics
- Overall winning party identification
- Comprehensive candidate performance analysis

### 3. Seat Allocation System
- **Proportional Seats**: 120 seats allocated based on vote share (1 seat per 100 votes)
- **Bonus Seats**: 10 bonus seats awarded to each regional winner
- **Total Calculation**: Sum of proportional and bonus seats

## 📈 Output Sections

The system generates the following detailed reports:

1. **Regional Results**
   - Total voters per region
   - Male and female voter counts
   - Candidate-wise vote breakdown
   - Regional winners

2. **Overall Election Summary**
   - Total voters across all regions
   - Gender distribution statistics
   - Overall winning party

3. **Seat Allocation**
   - Votes per party
   - Proportional seat calculation
   - Bonus seat allocation
   - Final seat distribution

## 🛠️ Technical Implementation

### Dependencies
```python
import numpy as np
import matplotlib.pyplot as plt
```
## Core Functions
```seat_calculation(vote_by_party, winner_list)```
Calculates parliamentary seat allocation using a mixed system:

- Proportional representation based on vote share

- Bonus seats for regional winners

### Data Processing
- 3D array manipulation using NumPy

- Statistical aggregation across multiple dimensions

- Winner determination using np.argmax()

## 🎯Usage
1. Data Input: Modify the votes_matrix to input new election data

2. Run Analysis: Execute the script to generate comprehensive results

3. Interpret Results: Review regional and overall outcomes

4. Visualize: Uncomment visualization section for graphical analysis

## 📋 Sample Output Structure
```text
----------- Election Result -----------

--------- Result of Region 1 ---------
Total voters: X
Total male voters: Y
Total female voters: Z

[Candidate Results...]

Winner from Region 1: [Party Name]

[Repeat for all regions...]

----------- Overall Result -----------
Total voters: [Total]
Total male voters: [Male Total]
Total female voters: [Female Total]
Overall maximum vote gained by: [Winning Party]

----------- Seat Allocation -----------
[Party Name]: Votes = [Count], Total Seats = [Number]
```
### 🔧 Customization
- Modify candidate_dict to add/remove political parties

- Adjust votes_matrix dimensions for different numbers of regions/candidates

- Change seat allocation parameters (total_seats_votes, bonus_per_region)

- Customize visualization parameters as needed

## 🤝 Contribution

Contributions are welcome! Whether it’s improving the logic, optimizing the code, or enhancing visualization — every contribution is appreciated.