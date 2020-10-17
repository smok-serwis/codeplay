
import pandas as pd
import random
import numpy as np
from sklearn import model_selection
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.svm import NuSVC
import math
from sklearn import metrics

pd.set_option('display.max_columns', None)
path1= r"C:\Users\Szymon\Desktop\Hackathon\KREDYTY.csv"
path2= r"C:\Users\Szymon\Desktop\Hackathon\POLISY.csv"
kredyty = pd.read_csv(path1, sep='\t', delimiter=',', encoding ="ISO-8859-1", error_bad_lines=False)
polisy = pd.read_csv(path2, sep='\t', delimiter=',', encoding ="ISO-8859-1", error_bad_lines=False)

polisy.set_index('ID_KLIENTA', inplace=True)
kredyty.set_index('ID_UMOWY', inplace=True)
loan_clients = { 'data': kredyty['WALUTA'], 'produkt': '1','cecha1':kredyty['GRUPA_RYZYKA'],'cecha2':kredyty['OPROCENTOWANIE']}
policy_clients = {'data': polisy['DATA_WAZNOSCI_OD'], 'produkt': '0','cecha1':polisy['KWOTA_SKLADKI'],'cecha2':polisy['RODZAJ_UBEZPIECZENIA']}

pd.DataFrame(loan_clients).dropna().to_csv('loan_clients.csv')
pd.DataFrame(policy_clients).dropna().to_csv('policy_clients.csv')

