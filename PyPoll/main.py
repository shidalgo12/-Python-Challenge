import os
import csv

# Path to collect data from the PyBank folder
poll_data = os.path.join('..', 'PyPoll', 'election_data.csv')

# Read in the CSV file
with open(poll_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Calculate Total Voters - COMPLETE
    #Voters = list(csvreader)
    # Total_Voters = len(Voters)-0
   
    #Build a List of individual Candidates
    Candidate_Names = []
    Candidate_Counts = {}
    for row in csvreader:
        Name = row[2]
        if Name not in Candidate_Names:
            Candidate_Names.append(Name)
            #Candidate_Counts = [Candidate_Names]=0

    print(*Candidate_Names)

    
    #for x in Candidate_Name:
        #print(Candidate_Name)   
    
    #Calculate Total # of Votes for Each Candidate
        #Voters_Per_Candidate =
    
    #  % of Votes for Each Candidate
        # Percentage_of_Voters = Voters_Per_Candidate/Total_Voters * 100
     
    #Identify the Winner of the Election
    
#Print Election Results
print("Election Results")
print("-------------------------")
#Print Total Voters
# print(f"Total Voters: {Total_Voters}")
print("-------------------------")
#Print Candidates and voter stats
#print(f"{Candidate_Name} {Percentage_of_Voters} ({Voters_Per_Candidate})")
print("-------------------------")
#Print Winner
#print("Winner: ")
print("-------------------------")


