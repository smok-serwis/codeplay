import csv
from scipy import stats
import pickle
obj = {}
#suma dochodu
#przeważający rodzaj dochodu

count = 0
users_list = []
with open('result.csv', newline='') as income:
    income_reader = csv.reader(income, delimiter=',')
    #Each row contain one income transaction, one 'amount'
    for row in income_reader:
        user = row[0]
        year = row[1].split('/')[0]
        amount = float(row[2])
        category = row[3]
        if not (year in obj):
            obj[year] = {}
        else:
            if not (user in obj[year]):
                obj[year][user] = {}
            else:
                if not (category in obj[year][user]):
                    #make single element list with first income data
                    obj[year][user][category] = [amount]
                else:
                    obj[year][user][category].append(amount)

for year in obj:
    for user in obj[year]:
        su = 0
        for category in obj[year][user]:
            su = sum(obj[year][user][category])
