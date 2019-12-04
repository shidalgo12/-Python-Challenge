import os
import csv

# Path to collect data from the PyBank folder
budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')
Total_Months = 0 

# Read in the CSV file
with open(budget_data, 'r', newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    Profit_Loss = []
    data = list(csvreader)
        
    # Calculate Total Months - COMPLETE
    for row in data:
        Total_Months = Total_Months + 1
    #Print Financial Analysis - COMPLETE
    print("Financial Analysis")
    print("----------------------------")
    #Print Total Months - COMPLETE
    print(f"Total Months: {Total_Months}")
    
    # Calculate Total Profit/Loss
      #Stuck on how to sum up Profit/Losses through a loop  
    # Calculate Monthly Change
    for i in range(1,len(data)):
        Date = data[i][0]
        # print(Date)
        Current_Total= int(data[i][1])
        # print(Current_Total)
        Previous_Total = int(data[i-1][1])
        # print(Previous_Total)
        Monthly_Change = Current_Total-Previous_Total
        # print(Monthly_Change)
        PL_Change = (Date,Monthly_Change)
        # print(PL_Change)
        # Change = list(PL_Change)
        # print(Change)
    
    # Calculate Average Change
    
    # for j in range(0,len(Change)):   
        # Total_Change = Total_Change + int(Change[j],[1]) + int(Change[j+1],[1])
        # Avg_Change = int 
        # print(Avg_Change)
        # Calculate Average Monthly Change
        # Avg_Change =  Sum of Monthly Change/Total_Months
        # print(Avg_Change)
    
    # for row in data:
        # for i in range(1,Total_Months):
            # Total = Total + int(data[i+1][1])
    
    # Calculate Total Profit/Loss
    # Total = (int(data[i][1]) + int(data[i+1][1]))
    # #Calculate Greatest Increase in Profits by Date & Amount
    #     #Max_PL_Change = max(PL_Change)
        
    #     # p=df['ColumnName'].max()
        
    # #Calculate Greatest Decrease in Profits by Date & Amount
    #     #Min_PL_Change = min(PL_Change)


# #Print Average Change
# print(f"Average Change: {Avg_Change}", round(Avg_Change,2))

#Print Greatest Increase in Profits
    #print(f"Greatest Increase in Profits : {Date} {max_increase}"

#Print Greatest Decrease in Profits
#print(f"Greatest Decrease in Profits : {Date} {max_decrease}"    