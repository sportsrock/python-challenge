# import dependancies 
import os
import csv

# Initialize variables
Total_votes = 0
Charles_Casper_Stockham_Votes = 0 
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_Votes = 0




# Grab the file path of our election_data
file_path = os.path.join('..', 'Resources', 'election_data.csv')


# Opening election_data
with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)


    # Skip the header
    header = next(reader)

    # Columns Ballot ID, County, Candidate
    Ballot_ID_index = header.index('Ballot ID')
    County_index = header.index('County')
    Candidate = header.index('Candidate')

   # Process each row in the CSV file
    for row in reader:
        
        # INcrement the total number of votes
        Total_votes += 1

        Candidate_name = row[2]
        if Candidate_name == "Charles Casper Stockham":
            Charles_Casper_Stockham_Votes += 1

        elif Candidate_name == "Diana DeGette":
            Diana_DeGette_votes += 1

        elif Candidate_name == "Raymon Anthony Doane":
            Raymon_Anthony_Doane_Votes += 1

        # Determine the candidate with the most votes
        winner_votes = max(Charles_Casper_Stockham_Votes, Diana_DeGette_votes, Raymon_Anthony_Doane_Votes)

        # Check the winner and print the result
        if winner_votes == Charles_Casper_Stockham_Votes:
            winner_name = "Charles Casper Stockham"
        elif winner_votes == Diana_DeGette_votes:
            winner_name = "Diana DeGette"
        else:
            winner_name = "Raymon Anthony Doane"

        Percentage_Charles = round((Charles_Casper_Stockham_Votes/ Total_votes) * 100,3) 
        Percentage_Diana = round((Diana_DeGette_votes/ Total_votes) * 100,3)
        Percentage_Raymon = round((Raymon_Anthony_Doane_Votes/ Total_votes) * 100,3)

        


# output
output = f"""Election Results
-------------------------
Total Votes: {Total_votes}
-------------------------
Charles Casper Stockham: {Percentage_Charles}% ({Charles_Casper_Stockham_Votes})
Diana DeGette: {Percentage_Diana}% ({Diana_DeGette_votes})
Raymon Anthony Doane: {Percentage_Raymon}% ({Raymon_Anthony_Doane_Votes})
-------------------------
Winner: {winner_name}"""

#print output
print(output)

# Specify the folder path where you want to save the file
output_folder = os.path.join('..', 'analysis')

# Save the output to a text file
output_file = os.path.join(output_folder, 'Election_results.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write(output)