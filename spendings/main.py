import csv

umowy_dict = {}
switch_row_12 = {
    "CODZIENNE_ZAKUPY": 0,
    "ZDROWIE": 1,
    "PODRÓ¯E": 2,
    "ZAKUPY_INT": 2,
    "SAMOCHÓD": 3,
    "UBRANIA": 4,
    "DLA_DOMU": 5,
    "BIUROWE": 5,
    "CZAS_WOLNY": 6,
    "DZIECI": 7,
    "RACHUNKI": 9,
    "RACHUNKI_DOMOWE": 9,
    "WYPLATA_BANKOMAT": 10,
}
switch_row_11 = {
    "WCZASY": 2,
    "PODRÓŻE": 2,
    "FAST_FOOD": 6,
    "RESTAURACJA": 6,
    "CHARYTATYWNE": 8,
    "WYP£ATA_GOTÓWKOWA": 10,
    "PAYU_PAYPAL": 11,
}
with open('UMOWY_STANY.csv', newline='') as umowy:
    reader_umowy = csv.reader(umowy, delimiter=',', quotechar='|')
    for row in reader_umowy:
        umowy_dict[row[1]] = row[2]
with open('input.csv', newline='', encoding="utf8") as csvfile:
    with open('output.csv', 'w', newline='', encoding="utf8") as out:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|', )
        writer = csv.writer(out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if float(row[4]) > 0 and (row[11] != '' or row[12] != ''):
                case_type = -1
                case_type = switch_row_12.get(row[12], -1)
                if case_type == -1:
                    case_type = switch_row_11.get(row[11], -1)
                if case_type >= 0:
                    try:
                        writer.writerow([umowy_dict[row[1][:-2]], row[0], row[4], case_type])
                    except KeyError:
                        print("Keyerror: " + row[1][:-2])
