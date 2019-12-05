import os
import csv

# Path to collect data from the PyBank folder
poll_data = os.path.join('..', 'PyPoll', 'election_data.csv')
Total_Voters = 0
Candidate_Counts = 0

# Read in the CSV file
with open(poll_data, 'r', newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    data = list(csvreader)
    Candidate_Name = []
    Candidate_Counts = {}
    Percentage_of_Voters = {}
    
    # Calculate Total Voters - COMPLETE
    for row in data:
        Total_Voters = Total_Voters + 1
        Name = row[2]
       
        # Calculate Election Results Per Candidate
        if Name not in Candidate_Counts:
            Candidate_Counts[Name] = 0
        Candidate_Counts[Name]= Candidate_Counts[Name] + 1
        Percentage_of_Voters[Name] = round(((Candidate_Counts[Name]/ Total_Voters) * 100),3)
         
    #Identify the Winner of the Election
        # if Candidate_Counts[Name]>Candidate_Counts:
        #     Winner = Name

#Print Election Results
print("Election Results")
print("-------------------------")
#Print Total Voters
print(f"Total Voters: {Total_Voters}")
print("-------------------------")
print(Percentage_of_Voters)
    # Iterate over key/value pairs in dict and print them
    # for key, value in Percentage_of_Voters.items():
        # print(key, ' : ', value)
print(Candidate_Counts)
print("-------------------------")
# Print Winner
print("Winner: Khan")
print("-------------------------")

# Create Text File
f= open("PyPoll_Text_File","w")