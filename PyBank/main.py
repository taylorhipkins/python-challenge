import os
import csv

# Path to the input file
budgetdata_csv = os.path.join("PyBank", "Resources", "budget_data.csv")
# Initialize variables
total_months = 0
net_total = 0
prev_profit_loss = 0
profit_changes = []
dates = []

# Read the CSV file
with open(budgetdata_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row
    for row in csvreader:
        # Count total months
        total_months += 1
        
        # get date and profit/loss
        date = row[0]
        dates.append(date)
        profit_loss = int(row[1])
        
        # Calculate net total amount of profit/losses
        net_total += profit_loss
        
        # Calculate changes in profit/losses
        if total_months > 1:
            change = profit_loss - prev_profit_loss
            profit_changes.append(change)
        prev_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_changes) / len(profit_changes)

# Find greatest increase and decrease 
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# Retrieve dates for greatest increase and decrease
increase_date = dates[profit_changes.index(greatest_increase) + 1]
decrease_date = dates[profit_changes.index(greatest_decrease) + 1]

# Prepare analysis results
analysis_results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})
"""

# Print analysis to terminal
print(analysis_results)

# Export analysis results to a text file
output_file = 'PyBank_Results.txt'
with open(output_file, 'w') as file:
    file.write(analysis_results)

    print(f"Results exported to '{output_file}'")
