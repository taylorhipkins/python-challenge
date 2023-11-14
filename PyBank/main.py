import os
import csv

# file path
budgetdata_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Initialize variables 
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Open and read the CSV file
with open(budgetdata_csv, 'r') as file:
    # Skip the header row
    header = next(file)

    # Loop through data
    for line in file:
        # Split the line into columns
        date, profit_loss = line.strip().split(',')

        # Convert profit_loss to an integer
        profit_loss = int(profit_loss)

        # Calculate total number of months
        total_months += 1

        # Calculate net total amount
        net_total += profit_loss

        # Calculate change in profit/loss
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            # Check for greatest increase
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            # Check for greatest decrease
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change
        # Update previous profit/loss 
        previous_profit_loss = profit_loss

# Calculate the sum of all changes
sum_changes = sum(changes)

# Calculate the average change
average_change = sum_changes / len(changes) if len(changes) > 0 else 0

# Print the results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")