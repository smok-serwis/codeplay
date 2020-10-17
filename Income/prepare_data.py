import csv
client_contract = {}
kategoria = {
    'STYPENDIUM': 0,
    'SOCJALNE': 1,
    'ZUS': 2,
}

with open('UMOWY_STANY.csv', newline='') as umowy_csvfile:
    umowy_reader = csv.reader(umowy_csvfile, delimiter=',')
    next(umowy_reader)
    lines = 0
    for row in umowy_reader:
        client_contract[row[1]] = row[2]
with open('operacje.csv', newline='') as operacje_csvfile:
    with open('result.csv', 'w', newline='', encoding='utf-8') as result:
        operacje_reader = csv.reader(operacje_csvfile, delimiter=';')
        result_writer = csv.writer(result, delimiter=',')
        next(operacje_reader)
        for row in operacje_reader:
            if float(row[3]) > 0 and row[4] != '':
                finder = -1
                finder = kategoria.get(row[4], -1)
                if finder != -1:
                    try:
                        result_writer.writerow([client_contract[row[1]], row[0], row[3], finder])
                    except KeyError:
                        print('KeyError: ' + row[1])
                else:
                    print(f'{row[4]}, {row[5]}')
