import os
import csv
import operator

# Path to collect data from the PyBank folder
poll_data = os.path.join('PyPoll', 'election_data.csv')
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
    
    # Calculate Total Voters
    for row in data:
        Total_Voters = Total_Voters + 1
        Name = row[2]
       
        # Calculate Election Results Per Candidate
        if Name not in Candidate_Counts:
            Candidate_Counts[Name] = 0
        Candidate_Counts[Name]= Candidate_Counts[Name] + 1
        Percentage_of_Voters[Name] = round((Candidate_Counts[Name]/ Total_Voters)*100,2)
         
    #Identify the Winner of the Election
    Winner = max(Candidate_Counts, key=Candidate_Counts.get)
    # print(Winner)

    # Combine Percentage_of_Voters and Candidate_Counts dictionaries by key
    result = {}
    for key in (Percentage_of_Voters.keys() | Candidate_Counts.keys()):
        if key in Percentage_of_Voters: result.setdefault(key, []).append(Percentage_of_Voters[key])
        if key in Candidate_Counts: result.setdefault(key, []).append(Candidate_Counts[key])
    # print(result)

    # Sort combined dictionaries by value in descending order
    sorted_result = dict(sorted(result.items(), key=operator.itemgetter(1),reverse=True))
    # print(sorted_result)

#Print Election Results
print("Election Results")
print("-------------------------")
#Print Total Voters
print(f"Total Voters: {Total_Voters}")
print("-------------------------")
for key in sorted_result:
    print(key, ':', sorted_result[key])
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")

# # Create Text File
# f= open("PyPoll_Text_File","w")