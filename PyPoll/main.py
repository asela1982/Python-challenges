# ## Option 2: PyPoll

# ![Vote-Counting](Images/Vote_counting.jpg)

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

import csv
import os
from collections import Counter

candidate = Counter()

votes = 0

filepath = os.path.join("raw_data","election_data_2.csv")

with open(filepath,'r') as file:
    csvreader = csv.reader(file,delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        votes = votes + 1
        candidate[row[2]] += 1


print("""Election Results
-------------------------""")
print(f"Total Votes: {votes}")
print("""-------------------------""")


candidate = dict(candidate)

for key,value in candidate.items():
    percentage = '{0:.1%}'.format(float(value)/float(votes))
    print(f"{key}: {percentage} ({value})")

print("""-------------------------""")

def keywithmaxvalue(dict):
    votes = list(dict.values())
    candidate = list(dict.keys())
    max_candidate = candidate[votes.index(max(votes))]
    max_votes = max(votes)
    print(f"Winner: {max_candidate}") 

keywithmaxvalue(candidate)

print("""-------------------------""")