import os
import csv

# Define the file path
election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")
#PyPoll/Resources/election_data.csv
# Initialize variables 
total_votes = 0
candidates = {}  # Create Dictionary 

# Open and read the CSV file
with open(election_data_csv, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    header = next(csv_reader)

    # Loop through each row 
    for row in csv_reader:
        # Get the candidate name from the row
        candidate = row[2]

        # Update total votes
        total_votes += 1

        # Update candidate votes in the dictionary
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop through candidates and calculate percentages
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")

# Find the winner based on popular vote
winner = max(candidates, key=candidates.get)
print(f"Winner: {winner}")
print("-------------------------")
