# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, 
# his concentration isn't what it used to be.)

# You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). 
# Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# * The total number of votes cast
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:

# ```
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------
# ```

# Your final script must be able to handle any such similarly-structured dataset in the future 
# (i.e you have zero intentions of living in this hillbilly town -- so your script needs to work
#  without massive re-writes). In addition, your final script should both print the analysis to 
# the terminal and export a text file with the results.

# import the dependencies
import csv
import os

# Set empty list variables
Voterid = []
County = []
Candidate = []

# file path
filepath = os.path.join("raw_data","election_data_2.csv")

# Open pypoll CSV
with open(filepath, 'r') as fh:
    csvReader = csv.reader(fh, delimiter=',')

    # Skip headers
    next(csvReader, None)

    for row in csvReader:

        # Append data from the row
        Voterid.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

mydict ={}
votes = 0

# get key with max value
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]




for item in Candidate:
    if item in mydict:
        mydict[item] = mydict[item]+1
    else:
        mydict[item] = 0
    votes += 1

print("""Election Results
-------------------------""")
print("Total Votes: {a:,}".format(a=votes))
print("-------------------------")
for key,value in mydict.items():
    perc = value/votes
    print("{a:}: {b:.2%} ({c:,})".format(a=key,b=perc,c=value) )
print("-------------------------")
print("Winner: {a:}".format(a=keywithmaxval(mydict)))
print("-------------------------")

