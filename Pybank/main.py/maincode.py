import os
import csv

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
change_list = []
greatest_increase_month = ""
greatest_increase_value = 0
greatest_decrease_month = ""
greatest_decrease_value = 0

# Grab the file path of our budget_data
file_path = os.path.join('..', 'Resources', 'budget_data.csv')

# Open budget_data
with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row
    header = next(reader)

    # Assuming the column names are 'Date' and 'Profit/Losses'
    date_column_index = header.index('Date')
    profit_loss_column_index = header.index('Profit/Losses')

    # Process each row in the CSV file
    for row in reader:
        # Extract the profit or loss from the second column
        profit_loss = int(row[profit_loss_column_index])

        # Update the total profit or loss
        total_profit_loss += profit_loss

        # Increment the total number of months
        total_months += 1

        # Calculate the change in profit or loss compared to the previous month
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            change_list.append(change)

            # Check for the greatest increase and decrease in profits
            if change > greatest_increase_value:
                greatest_increase_value = change
                greatest_increase_month = row[date_column_index]
            elif change < greatest_decrease_value:
                greatest_decrease_value = change
                greatest_decrease_month = row[date_column_index]
        
        # Set the current profit or loss as the previous for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = round(sum(change_list) / len(change_list), 2)

# Format the output
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_value})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_value})"""

# Print the output to the console
print(output)

# Specify the folder path where you want to save the file
output_folder = os.path.join('..', 'analysis')

# Save the output to a text file
output_file = os.path.join(output_folder, 'financial_analysis.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write(output)


