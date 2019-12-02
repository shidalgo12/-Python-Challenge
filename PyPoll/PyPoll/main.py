import os
import csv

# Path to collect data from the PyBank folder
poll_data = os.path.join('..', 'PyPoll', 'election_data.csv')

# Define the function and have it accept the 'poll_data' as its sole parameter
def election_results(poll_data):
    # Assign values to variables 
    Voter_ID = str(poll_data[0])
    County = str(poll_data[1])
    Candidate = str(poll_data[2])

# Read in the CSV file
with open(poll_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Calculate Total Voters - COMPLETE
    data = list(csvreader)
    Total_Voters = len(data)-0
    
    #Complete List of Candidates
    Candidates = list(csvreader[row[2]])
    for row in csvreader:
        Candidates[row[2]] = 0    

x = Candidates.keys() 
    
    #Calculate % of Votes for Each Candidate
        # Percentage_of_Voters = Candidate_Voters/Total_Voters * 100

    #Calculate Total # of Votes for Each Candidate
        #Candidate Voters = 
    #Identify the Winner of the Election
    
#Print Election Results
print("Election Results")
print("-------------------------")
#Print Total Voters
print(f"Total Voters: {Total_Voters}")
print("-------------------------")
#Print Candidates and voter stats
print(f"{x} : ")
print("-------------------------")
#Print Winner
#print("Winner: ")
print("-------------------------")


