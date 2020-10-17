import csv
from scipy.stats import kurtosis
import pickle


def average(arr):
    return sum(arr)/len(arr)


with open('transactions.csv', newline='', encoding="utf8") as csvfile:
    years = {}
    reader = csv.reader(csvfile, delimiter=',', quotechar='|', )
    for row in reader:
        user = row[0]
        date = row[1]
        amount = float(row[2])
        transaction_type = row[3]
        year = date.split('-')[0][-2:]
        if not (year in years):
            years[year] = {}
        else:
            if not (user in years[year]):
                years[year][user] = {}
            else:
                if not (transaction_type in years[year][user]):
                    years[year][user][transaction_type] = [amount]
                else:
                    years[year][user][transaction_type].append(amount)

for year in years:
    for user in years[year]:
        for transaction_type in years[year][user]:
            amounts = years[year][user][transaction_type]
            years[year][user][transaction_type] = {
                'count': len(amounts),
                'average': average(amounts),
                'kurtosis': kurtosis(amounts),
                'min': min(amounts),
                'max': max(amounts),
            }


file = open('dump.py', 'wb')
pickle.dump(years, file, -1)
