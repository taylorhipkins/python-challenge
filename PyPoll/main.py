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
PyPoll_results = "Election Results\n"
PyPoll_results += "-------------------------\n"
PyPoll_results += f"Total Votes: {total_votes}\n"
PyPoll_results += "-------------------------\n"

# Loop through candidates and calculate percentages
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    PyPoll_results += f"{candidate}: {percentage:.3f}% ({votes})\n"

PyPoll_results += "-------------------------\n"

# Find the winner based on popular vote
winner = max(candidates, key=candidates.get)
PyPoll_results += f"Winner: {winner}\n"
PyPoll_results += "-------------------------"

# Print analysis to terminal
print(PyPoll_results)

# Export analysis results to a text file
output_file = 'PyPoll_Results.txt'
with open(output_file, 'w') as file:
    file.write(PyPoll_results)

    print(f"Results exported to '{output_file}'")
