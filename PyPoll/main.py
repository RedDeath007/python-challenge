#importing os and csv
import os
import csv

#reading the file
election = os.path.join("Resources/election_data.csv")
election_output = os.path.join("analysis/election_analysis.txt")
#variables
total_votes = 0
candidate_list = []
candidate_votes = {}

#opening file
with open(election, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_votes[row[2]] = 0

        candidate_votes[row[2]] += 1  
        
with open (election_output, "w") as txtfile:

    output = (f'Election Results \n' 
        f' ------------------------- \n'
        f'Total Votes: {total_votes} \n'
        f' -------------------------\n')
    print(output, end="")
    txtfile.write(output)
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent = round((votes / total_votes) * 100, 3)
        voter_output = f"{candidate}: {percent}% ({votes})\n"
        print(voter_output, end="")
        txtfile.write(voter_output)

    winner = max(candidate_votes, key=candidate_votes.get)
    winner_output = (f'------------------------- \n'
                     f'Winner: {winner}\n'
                     f'-------------------------')
    print(winner_output)
    txtfile.write(winner_output)
    


    