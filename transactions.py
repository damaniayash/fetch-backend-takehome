import csv
from datetime import datetime
import json
import argparse

# Setting up amount to be spend as an arguement
parser = argparse.ArgumentParser()
parser.add_argument('-s','--spend', type=int, required=True)
args = parser.parse_args()

# Defining the transaction class
class Transaction:
    def __init__(self, payer, points, timestamp):
        self.payer = payer
        self.points = points
        self.timestamp = timestamp

# t_list contains all the transactions from the transaction.csv
t_list = []
try:
    with open('transactions.csv',) as csvfile:
        reader = csv.reader(csvfile)
        # skipping the headers
        next(reader)
        for row in reader:
            # creating transaction objects and adding them to t_list
            transaction = Transaction(row[0], int(row[1]), datetime.strptime(row[2],'%Y-%m-%dT%H:%M:%SZ'))
            t_list.append(transaction)
except FileNotFoundError:
    raise Exception('Make sure the file name is transactions.csv and is in the same directory as this program')
t_list

# Sorting the transaction list based on the timestamp such that oldest transactions are at the top
t_list = sorted(t_list, key=lambda t:t.timestamp)


total_points = 0
spent_points = 0
points_to_spend = args.spend

# Calculating the total points and sum of points for "spend" transaction
for t in t_list:
    total_points += t.points
    if t.points < 0:
        spent_points += t.points

# If the passed spend arguement is larger than the total points that the user has we raise an exception
if points_to_spend > total_points:
    raise Exception("Cannot spend more points than you have!")

# Adding the already spent points to points to spend so when we traverse the t_list, we can skip them
points_to_spend += abs(spent_points)

j=0
# break the loop if points_to_spend is zero / all transactions are completed
while points_to_spend >= 0 and j <= len(t_list)-1:
    
    # if the points are negative, it means that the user spent these points already, we can skip them as we already added them to points to spend
    if t_list[j].points < 0:
        t_list[j].points = 0
        j+=1
        continue    
    
    # if points_to_spend is larger than the current transaction points then we can directly subtract the points
    elif points_to_spend >= t_list[j].points:
        points_to_spend -= t_list[j].points
        t_list[j].points = 0
        
    # if points_to_spend is smaller than the current points then we can update payer's points as whatever is left after spending the points 
    elif points_to_spend < t_list[j].points:
        t_list[j].points -= points_to_spend
        points_to_spend = 0
    j+=1

# Create a dictionary with payer name and point balances
payer_dict = {}
for i in range(0, len(t_list)):
    payer_dict[t_list[i].payer] = payer_dict.get(t_list[i].payer, 0) + t_list[i].points   
r = json.dumps(payer_dict,indent=4)

print(r)
with open('payers.json', 'w') as fp:
    json.dump(payer_dict, fp,indent=4)
