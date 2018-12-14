
import csv
import os

poll_df = os.path.join("Resources","election_data.csv")



print("Election Results")
print("--------------------")

khan_total = 0

with open(poll_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    vote_count = sum(1 for vote in csvfile)
    print(f"Total Votes: {vote_count}")

with open(poll_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in (csvreader):
        if row[2] == "Khan":
            khan_total = khan_total + 1
            
khan_percent = khan_total/vote_count

khan_dec = round(khan_percent, 2)
        
print(f'Khan Total: {khan_total}')
#print(f"Khan Market Share:  {khan_percent}")
#print (round(khan_percent, 2))

print (khan_dec)*100
    
#>>> words = “This is random text we’re going to split apart”
 
#>>> words2 = words.split(“ “)
 
#>>> words2
    