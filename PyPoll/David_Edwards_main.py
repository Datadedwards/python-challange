
import csv
import os

poll_df = os.path.join("Resources","election_data.csv")

khan = "Khan"
correy = "Correy"
li = "Li"
otooley = "O'Tooley"

khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

with open(poll_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    vote_count = sum(1 for vote in csvfile)

with open(poll_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in (csvreader):
        if row[2] == (khan):
            khan_total = khan_total + 1  
        elif row[2] == (correy):
            correy_total = correy_total + 1 
        elif row[2] == (li):
            li_total = li_total + 1
        elif row[2] == (otooley):
            otooley_total = otooley_total + 1

if khan_total > correy_total and khan_total > li_total and khan_total > otooley_total:
    winner = ("Khan")
elif correy_total > khan_total and correy_total > li_total and correy_total > otooley_total:
     winner = ("Correy")
elif li_total > khan_total and li_total > correy_total and li_total > otooley_total:
     winner = ("Li")
elif otooley_total > correy_total and otooley_total > li_total and otooley_total > khan_total:
     winner = ("O'Tooley")

candidate_1 = {"name": "Khan",  "voteamount" : khan_total}
candidate_2 = {"name": "Correy",  "voteamount" : correy_total}
candidate_3 = {"name": "Li",  "voteamount" : li_total}
candidate_4 = {"name": "O'Tooley",  "voteamount" : otooley_total}

khan_percent = khan_total/vote_count
khan_dec = round(khan_percent, 2)

correy_percent = correy_total/vote_count
correy_dec = round(correy_percent, 2)

li_percent = li_total/vote_count
li_dec = round(li_percent, 2)

otooley_percent = otooley_total/vote_count
otooley_dec = round(otooley_percent, 2)


print("Election Results")
print("--------------------")
print(f"Total Votes: {vote_count}")
print("--------------------")
print(" " + str(khan) + ": {:.2%}".format(khan_dec) + " (" + str(khan_total) +")")
print(" " + str(correy) + ": {:.2%}".format(correy_dec) + " (" + str(correy_total) +")")
print(" " + str(li) + ": {:.2%}".format(li_dec) + " (" + str(li_total) +")")
print(" " + str(otooley) + ": {:.2%}".format(otooley_dec) + " (" + str(otooley_total) +")")
print("--------------------")
print(f"Winner: " + (winner))
print("--------------------")


file = open("main.txt", "w")
file.write("Election Results")
file.write("\n")
file.write("--------------------")
file.write("\n")
file.write(f"Total Votes: {vote_count}")
file.write("\n")
file.write("--------------------")
file.write("\n")
file.write(str(khan) + ": {:.2%}".format(khan_dec) + " (" + str(khan_total) +")")
file.write("\n")
file.write(str(correy) + ": {:.2%}".format(correy_dec) + " (" + str(correy_total) +")")
file.write("\n")
file.write(str(li) + ": {:.2%}".format(li_dec) + " (" + str(li_total) +")")
file.write("\n")
file.write(str(otooley) + ": {:.2%}".format(otooley_dec) + " (" + str(otooley_total) +")")
file.write("\n")
file.write("--------------------")
file.write("\n")
file.write(f"Winner: " + (winner))
file.write("\n")
file.write("--------------------")

file.close()





    

    