"""
In this challenge, you are tasked with creating a Python script for analyzing the financial records 
of your company. You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). 
Each dataset is composed of two columns: `Date` and `Revenue`. 
(Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset

The total amount of revenue gained over the entire period

The average change in revenue between months over the entire period

The greatest increase in revenue (date and amount) over the entire period

The greatest decrease in revenue (date and amount) over the entire period

As an example, your analysis should look similar to the one below:
"""

"""
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
"""

# import the libaries
import csv
import os

# filepath to the csv files
filepath = os.path.join("raw_data","budget_data_1.csv")

# lists to store data
list_month = []
list_revenue = []

print(
"""
Financial Analysis
----------------------------
"""
)

with open (filepath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    months = 0
    totrevenue = 0
    
    for row in csvreader:
        revenue = int(row[1])
        totrevenue = totrevenue + revenue
        months = months + 1

        #add revenue
        list_revenue.append(revenue)

        #add month
        list_month.append(row[0])

    print(f"Total Months: {months}")
    print(f"Total Revenue: ${totrevenue}")

# define a function to get the average value of a list of number
def average(list):
    total = sum(list)
    return total/len(list)

# using a list comprehension, construct a list that contains the difference 
# between the two corresponding elements
revenue_change_amount = [x - list_revenue[i - 1] for i, x in enumerate(list_revenue)][1:]

# call the avearge function on the above list
print(f"Average Revenue Change: {average(revenue_change_amount)}")

revenue_change_month = list_month[1:]

# create a dictionary by Zip lists together
revenue_change_dict = dict(zip(revenue_change_month,revenue_change_amount))


# define a function to get the max value(change in revenue) in a dict and its correponding key(month)
def greatestincrease(dict): 
    k=list(dict.keys())
    v=list(dict.values())
    maxval = max(v)
    month = k[v.index(maxval)]
    print(f"Greatest Increase in Revenue: {month} (${maxval})")

# define a function to get the min value(change in revenue) in a dict and its correponding key(month)
def greatestdecrease(dict): 
    k=list(dict.keys())
    v=list(dict.values())
    minval = min(v)
    month = k[v.index(minval)]
    print(f"Greatest Decrease in Revenue: {month} (${minval})")


greatestincrease(revenue_change_dict)
greatestdecrease(revenue_change_dict)
