import os
import csv

# Path to collect data from the PyBank folder
budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')

# Define the function and have it accept the 'budget_data' as its sole parameter
def print_finances(budget_data):
    # Assign values to variables 
    Date = str(budget_data[0])
    Profit_Loss = int(budget_data[1])

# Read in the CSV file
with open(budget_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    Total = 0

    #Calculate Total Months - COMPLETE
    data = list(csvreader)
    Total_Months = len(data)-0

    #Calculate Total Profit/Loss  
    #for row in csvreader:
       = Total += Profit_Loss

#Calculate Average Change
    for i in range(1,Total_Months):
    #Calculate Average Change in Profit/Loss per Month   
        #PL_Change = Profit_Loss[i] - Profit_Loss[i-1]
        #Avg_Change = PL_Change / Total_Months
    
    #Calculate Greatest Increase in Profits by Date & Amount
        #Max_PL_Change = max(PL_Change)
        
        # p=df['ColumnName'].max()
        
    #Calculate Greatest Decrease in Profits by Date & Amount
        #Min_PL_Change = min(PL_Change)

#Print Financial Analysis - COMPLETE
print("Financial Analysis")
print("----------------------------")

#Print Total Months - COMPLETE
    #print(f"Total Months: {Total_Months}")
print(f"Total Months: {Total_Months}")

#Print Total Profit/Loss
print(f"Total: {Grand_Total})
#Print Average Change
print(f"Average Change: {Avg_Change})"

#Print Greatest Increase in Profits
    #print(f"Greatest Increase in Profits : {Date} {max_increase}"

#Print Greatest Decrease in Profits
#print(f"Greatest Decrease in Profits : {Date} {max_decrease}"    