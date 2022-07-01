# Election_Analysis

## Project Overview
The Elections Board has requested that an election audit of a recent local congressional race be completed.

Determine the total number of ballots cast.
Obtain a comprehensive list of all candidates who earned votes.
Calculate the total number of votes received by each contender.
Determine the total number of votes garnered by each contender.
Determine the proportion of votes each contender received.
Decide the election winner based on popular vote.

## Resources

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.68.1

## Election-Audit Results

### - 1.Total number of votes cast in the election.

![1  Total_votes](https://user-images.githubusercontent.com/105666905/176813976-3e7d2446-b998-48ee-ba23-99d5920e9c4e.png)

### - 2.Number of votes and percentage of total votes.

![count_percentage(1)](https://user-images.githubusercontent.com/105666905/176814507-6417e702-4a7e-45f6-a1cf-588ffdf3a2d3.png)
![count_percentage(2)](https://user-images.githubusercontent.com/105666905/176814519-998d25a8-81f1-4a51-8893-a1fed1432f51.png)

### - 3.Country with the largest number of votes.

![Largest_county_votes](https://user-images.githubusercontent.com/105666905/176815774-69a7c45f-c066-45ec-9b80-2e0c432c8dff.png)
![Largest_county_votes(1)](https://user-images.githubusercontent.com/105666905/176815782-7bb2e056-bfd1-4d51-af74-7f9f6cc204fa.png)

### - 4.Canidate votes

![Candidate_votes_percentage](https://user-images.githubusercontent.com/105666905/176815448-1a90d00a-63d6-4b68-a114-6bec6abd22fb.png)

### - 5.Election winner

![Election_winner](https://user-images.githubusercontent.com/105666905/176817550-b87b0138-6a4f-40d6-a8c7-894fbc98ca57.png)

Cont'd:
1. Total Votes Cast
- 369,711
2. Number of votes and the percentage yielded for the county's
- County Votes:
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)
3. County with the largest vote count
- Denver
4. Number of votes cast and percentage of votes cast for each candidate
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)
5. Count and percentage of votes cast for the winning candidate
-Winner: Diana DeGette
-Winning Vote Count: 272,892
-Winning Percentage: 73.8%



## Election-Audit Summary

This script may be used to obtain total votes by county, resulting in votes per county and the percentage of votes cast in each precinct.It returns the county with the most votes in a visually appealing way.Provide a breakdown of the number of votes cast and the percentage of total votes cast for each candidate.Finally, it returns the winning candidate's vote total and total votes received.

- Refactoring 
With a few changes, we can add more lists/dictionaries to function on a larger number of vote casts. Refactor the Python script so that it may take generic csv files with no hardcoded names. Show a map of Colorado with demographic data placed over it.


