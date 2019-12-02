<<<<<<< HEAD
import os
import csv

# Path to collect data from the PyBank folder
poll_data = os.path.join('..', 'PyPoll', 'election_data.csv')

# Read in the CSV file
with open(poll_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Candidate = str(csvreader[2])
    #Candidate_Name = {rows[0]:rows[1] for rows in reader}
    mydict = {rows[0]:rows[1] for rows in csvreader}
    print(mydict[0])
    #Calculate Total Voters - COMPLETE
    #Voters = list(csvreader)
    # Total_Voters = len(Voters)-0
    #Complete List of Candidates
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
print(f"Total Voters: {Total_Voters}")
print("-------------------------")
#Print Candidates and voter stats
#print(f"{Candidate_Name} {Percentage_of_Voters} ({Voters_Per_Candidate})")
print("-------------------------")
#Print Winner
#print("Winner: ")
print("-------------------------")


=======
import os
import csv

# Path to collect data from the PyBank folder
poll_data = os.path.join('..', 'PyPoll', 'election_data.csv')

def election_results(poll_data):
    # Assign values to variables 
    Voter_ID = str(poll_data[0])
    County - str(poll_data[1])
    Candidate = str(poll_data[2])
    

# Read in the CSV file
with open(poll_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    Candidate_Name = {csvreader[2]} 
    
    #Calculate Total Voters - COMPLETE
    Voters = list(csvreader)
    Total_Voters = len(Voters)-0
    
    #Complete List of Candidates
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
print(f"Total Voters: {Total_Voters}")
print("-------------------------")
#Print Candidates and voter stats
#print(f"{Candidate_Name} {Percentage_of_Voters} ({Voters_Per_Candidate})")
print("-------------------------")
#Print Winner
#print("Winner: ")
print("-------------------------")


>>>>>>> 97742f5525a074ce24bb2105e74e65eb3680130f
