import csv
import os

budget_df = os.path.join("Resources","budget_data.csv")

## This is the title of the script DONE
print("Financial Analysis")
print("--------------------")

# Obviously we need a for loop to go through each row
# we need a way to caputure sum values of months, net amount
# we need a way to caputure and calculate average
# we need an if statement on greatest increase in profits
# and another if statement on greatest decrease in profits



# Calculate total number of months in the data set DONE

with open(budget_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    month_count = sum(1 for month in csvfile)
    print(f"Total Months: {month_count}")

with open(budget_df, newline="") as csvfile:
    csv_header = next(csvfile)
    
    total = 0
    for row in csv.reader(csvfile):
        total += int(row[1])
    print (f"Total: ${total}")
    
    
    def average(row[1]):
        col_l = len(row[1])
        
        for number in row[1]s:
            total += number
            return total / col_l
print(col_l)

# calculate total net amount of profit/loss over the entire period



# calculate aveage change in Profit/Losses between months over the entire period


# calculate greatest increase in profits (date and amount) over the entire period

# calculate greatest decrease in losses (date and amount) over the entire period

# print the analysis to the terminal and export a text file with the results (could be already existing text file, or create a readme file (bookmarked))


