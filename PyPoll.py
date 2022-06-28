# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes

#--------------------------------------------------------
# Import the datetime class from the date module.
import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

# Print the present time.
print("The time right now is ", now)

# ---------------
import csv

import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:


    # Read the file object with the render function.
    file_reader = csv.reader(election_data)


    # Read the header row.
    headers = next(file_reader)
        
        
    #print each row in the CSV file.
    for row in file_reader:
        #2. Addd to the total vote count.
        total_votes += 1

    # Print the canidate name from each row
        candidate_name = row[2]

     # If the candidate does not match any existing candiddate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1

# Detrmine the percentage of vote for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. if true then set winning_count = votes and wining_percent =
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")



    
# to do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)







#------------------------------------------

# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.

with open(file_to_save, "w") as txt_file:

# write some data to the file.

    txt_file.write("Counties in the Election \n--------------------------- \nArapahoe\nDenver\nJefferson")

#--------------------------------------------



