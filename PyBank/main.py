import os
import csv

# Path to collect data from the PyBank folder
budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')

# Read in the CSV file
with open(budget_data, 'r', newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    
    #Calculate Total Months - COMPLETE
    data = list(csvreader)
    Total_Months = len(data)-0
    
    #Calculate Total Profit/Loss
    # for i in range(1,Total_Months):
    # Total = int(data[i][1]) + int(data[i+1][1])
    # Calculate Average Change
    for i in range(1,len(data)):
        # print(data[i])
        Current_Total= int(data[i][1])
        # print(Current_Total)
        Previous_Total = int(data[i-1][1])
        #print(data[i][0],Current_Total,Previous_Total, Current_Total-Previous_Total)
        Monthly_Change = Current_Total-Previous_Total
        # Calculate Average Monthly Change
        # Avg_Change = Sum of Monthly Change/Total_Months
        # print(Avg_Change)

    #Calculate Greatest Increase in Profits by Date & Amount
        #Max_PL_Change = max(PL_Change)
        
        # p=df['ColumnName'].max()
        
    #Calculate Greatest Decrease in Profits by Date & Amount
        #Min_PL_Change = min(PL_Change)

#Print Financial Analysis - COMPLETE
    print("Financial Analysis")
    print("----------------------------")

#Print Total Months - COMPLETE
    print(f"Total Months: {Total_Months}")

#Print Total Profit/Loss
# print(f"Total: {Total}")
# #Print Average Change
# print(f"Average Change: {Avg_Change}", round(Avg_Change,2))

#Print Greatest Increase in Profits
    #print(f"Greatest Increase in Profits : {Date} {max_increase}"

#Print Greatest Decrease in Profits
#print(f"Greatest Decrease in Profits : {Date} {max_decrease}"    