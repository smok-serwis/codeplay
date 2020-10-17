import csv
from scipy import stats
import pickle
obj = {}
clients = {}
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
                obj[year][user] = [amount]
            else:
                obj[year][user].append(amount)

with open('KLIENCI.csv', newline='') as klienci:
    clients_reader = csv.reader(klienci, delimiter=',')
    next(clients_reader)
    for row in clients_reader:
        user_id = row[0]
        user_birthday = row[3]
        user_sex = row[4]
        clients[user_id] = [user_birthday, user_sex]


for year in obj:
    for user in obj[year]:
        # print(f'{user}-{year} {sum(obj[year][user])}')
        if user in clients:
            users_list.append([f'{user}-{year}', sum(obj[year][user]), clients[user][0], clients[user][1]])
print(users_list)
