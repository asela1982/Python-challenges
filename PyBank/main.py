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

 
# lists to store monthly revenue data
list_month = []
list_revenue = []


with open (filepath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader) #store the first row the csv file in a header variable
    months = 0 
    totrevenue = 0
    
    for row in csvreader:
        revenue = int(row[1])
        totrevenue = totrevenue + revenue
        months = months + 1

        #add monthly revenue to the list
        list_revenue.append(revenue)

        #add month to the list
        list_month.append(row[0])

    print(
"""
Financial Analysis
----------------------------
"""
    )
    print(f"Total Months: {months}")
    print(f"Total Revenue: ${totrevenue}")


# define a function to get the average value of a list of number
def average(list):
    total = sum(list)
    return total/len(list)


# using a list comprehension, construct a list that contains the difference 
# between the two corresponding elements
revenue_change_amount = [x - list_revenue[i - 1] for i, x in enumerate(list_revenue)][1:]

# call the average function on the above list
print(f"Average Revenue Change: {average(revenue_change_amount)}")

# list with the base month for the corresponding revenue change
revenue_change_month = list_month[:-1]

# create a dictionary by Zip lists together
revenue_change_dict = dict(zip(revenue_change_month,revenue_change_amount))

# write a function to get the max value(change in revenue) in a dict and its correponding key(month)
def greatestincrease(dict): 
    k=list(dict.keys())
    v=list(dict.values())
    maxval = max(v)
    month = k[v.index(maxval)]
    return(f"Greatest Increase in Revenue: {month} (${maxval})")

# write a function to get the min value(change in revenue) in a dict and its correponding key(month)
def greatestdecrease(dict): 
    k=list(dict.keys())
    v=list(dict.values())
    minval = min(v)
    month = k[v.index(minval)]
    return(f"Greatest Decrease in Revenue: {month} (${minval})")

# print the output to the terminal by calling the above functions
print(greatestincrease(revenue_change_dict))
print(greatestdecrease(revenue_change_dict))


# print the output to a text file
with open("Output.txt", "w") as text_file:
    text_file.write("""
Financial Analysis
----------------------------
""")
    text_file.write(f"Total Months: {months}"+ '\n')
    text_file.write(f"Total Revenue: ${totrevenue}"+ '\n')
    text_file.write(f"Average Revenue Change: {average(revenue_change_amount)}"+ '\n')
    text_file.write(greatestincrease(revenue_change_dict)+ '\n')
    text_file.write(greatestdecrease(revenue_change_dict)+ '\n')
