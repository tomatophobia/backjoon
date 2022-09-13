import pandas as pd
import numpy as np
import openpyxl

YTM = pd.read_excel('rf_ytm.xlsx', engine='openpyxl')
YTM['YTM'] = YTM['YTM'] / 100

BSTR = pd.DataFrame(np.zeros(20).reshape(10, 2), columns=['Year', 'YTM'])
for i in BSTR.index:
    BSTR.iloc[i, 0] = i + 1

for i in BSTR.index:
    for j in YTM.index:
        if BSTR.loc[i, 'Year'] == YTM.loc[j, 'Month'] / 12:
            BSTR.loc[i, 'YTM'] = YTM.loc[j, 'YTM']

for i in BSTR.index:
    if BSTR.loc[i, 'YTM'] == 0:
        j = 1
        while BSTR.loc[i + j, 'YTM'] == 0:
            j = j + 1
            if BSTR.loc[i + j, 'YTM'] > 0:
                break
        BSTR.loc[i, 'YTM'] = BSTR.loc[i - 1, 'YTM'] + (BSTR.loc[i + j, 'YTM'] - BSTR.loc[i - 1, 'YTM']) / (j + 1)

BSTR['SR'] = 0
BSTR['C'] = BSTR['YTM']
BSTR['DFPVC'] = 0
BSTR['LP'] = BSTR['C'] + 1
BSTR['PVC'] = 0
BSTR['PYLP'] = 0
BSTR.loc[0, 'SR'] = BSTR.loc[0, 'YTM']
BSTR.loc[0, 'PVLP'] = 1

for i in BSTR.index:
    if i >= 1:
        BSTR.loc[i, 'DFPVC'] = BSTR.loc[i - 1, 'DFPVC'] + (1 / (1 + BSTR.loc[i - 1, 'SR'])) ** BSTR.loc[i - 1, 'Year']
        BSTR.loc[i, 'PVC'] = BSTR.loc[i, 'C'] * BSTR.loc[i, 'DFPVC']
        BSTR.loc[i, 'PVLP'] = 1 - BSTR.loc[i, "PVC"]
        BSTR.loc[i, 'SR'] = (BSTR.loc[i, 'LP'] / BSTR.loc[i, 'PVLP']) ** (1 / BSTR.loc[i, 'Year']) - 1

print(BSTR)
