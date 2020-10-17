import os
import glob
import pandas as pd

os.chdir('files')
files = ['operacje1.csv', 'operacje2.csv', 'operacje3.csv', 'operacje4.csv', 'operacje5.csv', 'operacje6.csv',
         'operacje7.csv', 'operacje8.csv', 'operacje9.csv', 'operacje10.csv', 'operacje11.csv', 'operacje12.csv',
         'operacje13.csv']
csvv = pd.read_csv(files[0], delimiter=';', header=0)
print(csvv.head(5))
c_csv = pd.concat([pd.read_csv(f, delimiter=';', header=0) for f in files])
print(c_csv.head(5))
os.chdir('./')
c_csv.to_csv('../operacje.csv', sep=';', index=False, encoding='utf-8-sig')
