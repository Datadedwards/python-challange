import csv
import os

budget_df = os.path.join("Resources","budget_data.csv")


total = 0
change = 0
minvalue = 0
maxvalue = 0
average = 0


with open(budget_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    month_count = sum(1 for month in csvfile)


with open(budget_df, newline="") as csvfile:
    csv_header = next(csvfile)
    
    for row in csv.reader(csvfile):
        total += int(row[1])
        change -= int(row[1])

with open(budget_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv.reader(csvfile):
        value = float(row[1])
        minvalue = min(minvalue, value)
        maxvalue = max(maxvalue, value)

with open(budget_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    average = int(total/month_count)
        
print("Financial Analysis")
print("--------------------")       
print(f"Total Months: {month_count}")       
print(f"Total: ${total}")
print(f"Average per month: ${average}")
print(f"Greatest Increase in Profits: " + "${:}".format(maxvalue))
print("Greatest Decrease in Profits: " + "${:}".format(minvalue))
    

file = open("main.txt", "w")
file.write("Financial Analysis")
file.write("\n")
file.write("--------------------")
file.write("\n")
file.write(f"Total Months: {month_count}")
file.write("\n")
file.write(f"Total: ${total}")
file.write("\n")
file.write(f"Average per month: ${average}")
file.write("\n")
file.write("Greatest Increase in Profits: " + "${:}".format(maxvalue) +")")
file.write("\n")
file.write("Greatest Decrease in Profits: " + "${:}".format(minvalue) +")")
file.write("\n")

file.close()


