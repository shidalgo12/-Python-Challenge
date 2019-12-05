import os
import csv

# Path to collect data from the PyBank folder
budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')

Total_Months = 0
Total_PL = 0
Total_Change = 0
Max_Change = 0
Min_Change = 0

# Read in the CSV file
with open(budget_data, 'r', newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    data = list(csvreader)
    
    # Calculate Total Months
    for row in data:
        Total_Months = Total_Months + 1
     
    # Calculate Average Change
    for i in range(1,len(data)):
        Date = data[i][0]
        Current_Total= int(data[i][1])
        Previous_Total = int(data[i-1][1])
        Monthly_Change = Current_Total-Previous_Total
        Total_Change = Total_Change + Monthly_Change
 
        Average_Change = round((Total_Change/(Total_Months-1)),2)
       
        # Calculate Min and Max Changes
        PL_Change = (Date,Current_Total,Monthly_Change)
        if Monthly_Change > Max_Change:
            Max_Change = Monthly_Change
            Max_Date = (Date)
        elif Monthly_Change < Min_Change:
            Min_Change = Monthly_Change
            Min_Date = (Date)
    # Calculate Total Profit/Loss
    for i in range(0,len(data)):
        Profit_Loss = int(data[i][1])
        Total_PL = Total_PL + Profit_Loss
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_PL}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {Max_Date} (${Max_Change})")
print(f"Greatest Decrease in Profits: {Min_Date} (${Min_Change})")

#Create Text File
f= open("PyBank_Text_File","w")