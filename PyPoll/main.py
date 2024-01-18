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

    #adding candidate list
    for row in csvreader:
        #collecting total votes
        total_votes = total_votes + 1
        #recognize new candidate
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            #adding candidate votes
            candidate_votes[row[2]] = 0
        #adding votes to candidate already in list
        candidate_votes[row[2]] += 1  
#beginning output file
with open (election_output, "w") as txtfile:
    #formatting output
    output = (f'Election Results \n' 
        f' ------------------------- \n'
        f'Total Votes: {total_votes} \n'
        f' -------------------------\n')
    #terminal output 1
    print(output, end="")
    #textfile output 1
    txtfile.write(output)
    #combining candidate percentage and vote count outputs to be on the same line with one another
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent = round((votes / total_votes) * 100, 3)
        voter_output = f"{candidate}: {percent}% ({votes})\n"
        #terminal output 2
        print(voter_output, end="")
        #textfile output 2
        txtfile.write(voter_output)

    winner = max(candidate_votes, key=candidate_votes.get)
    winner_output = (f'------------------------- \n'
                     f'Winner: {winner}\n'
                     f'-------------------------')
    #terminal output 3
    print(winner_output)
    #textfile output 3
    txtfile.write(winner_output)
    


    