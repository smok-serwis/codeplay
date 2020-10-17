import csv
with open('result.csv', newline='') as income:
    income_reader = csv.reader(income, determiner=',')
    for row in income_reader:
        print('')