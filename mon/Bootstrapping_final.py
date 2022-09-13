from time import strftime
import pandas as pd
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta

YTM = pd.read_excel('ytm.xlsx')
YTM['YTM_rf'] = YTM['YTM_rf']/100
YTM['YTM_rd'] = YTM['YTM_rd']/100

issue_date = date(2020, 1, 1)
maturity_date = date(2030, 1, 1)


#무위험이자율 bootstraping_rf
bootstraping_rf = pd.DataFrame(np.zeros(30).reshape(10, 3), columns = ['Year', 'Date', 'YTM_rf'])
for i in bootstraping_rf.index:
    bootstraping_rf.iloc[i, 0] = i + 1
    bootstraping_rf.iloc[i, 1] = issue_date + relativedelta(years=i+1)

for i in bootstraping_rf.index:
    for j in YTM.index:
        if bootstraping_rf.loc[i, 'Year'] == YTM.loc[j, 'Month']/12:
            bootstraping_rf.loc[i, 'YTM_rf'] = YTM.loc[j, 'YTM_rf']


for i in bootstraping_rf.index:
    if bootstraping_rf.loc[i, 'YTM_rf'] == 0:
        j = 1
        while bootstraping_rf.loc[i + j, 'YTM_rf'] == 0:
            j = j + 1
            if bootstraping_rf.loc[i + j, 'YTM_rf'] > 0:
                break
        bootstraping_rf.loc[i, 'YTM_rf'] = bootstraping_rf.loc[i - 1, 'YTM_rf'] + (bootstraping_rf.loc[i + j, 'YTM_rf'] \
            - bootstraping_rf.loc[i - 1, 'YTM_rf'])/ (j+1)

bootstraping_rf['spot_rf'] = 0
bootstraping_rf['coupon_rf'] = bootstraping_rf['YTM_rf']
bootstraping_rf['DFPVC_rf'] = 0
bootstraping_rf['LP_rf'] = bootstraping_rf['coupon_rf'] + 1
bootstraping_rf['PVC_rf'] = 0
bootstraping_rf['PYLP_rf'] = 0
bootstraping_rf.loc[0, 'spot_rf'] = bootstraping_rf.loc[0, 'YTM_rf']
bootstraping_rf.loc[0, 'PVLP_rf'] = 1

for i in bootstraping_rf.index:
    if i >= 1:
        bootstraping_rf.loc[i, 'DFPVC_rf'] = bootstraping_rf.loc[ i - 1, 'DFPVC_rf'] + (1/(1 + bootstraping_rf.loc[ i-1, 'spot_rf'])) \
            ** bootstraping_rf. loc[i-1, 'Year']
        bootstraping_rf.loc[i, 'PVC_rf'] = bootstraping_rf.loc[i, 'coupon_rf'] * bootstraping_rf.loc[i, 'DFPVC_rf']
        bootstraping_rf.loc[i, 'PVLP_rf'] = 1 - bootstraping_rf.loc[i, "PVC_rf"]
        bootstraping_rf.loc[i, 'spot_rf'] = (bootstraping_rf.loc[i, 'LP_rf'] / bootstraping_rf. loc[i, 'PVLP_rf']) \
            ** (1 / bootstraping_rf.loc[i, 'Year']) - 1

#위험이자율 bootstraping_rd
bootstraping_rd = pd.DataFrame(np.zeros(30).reshape(10, 3), columns = ['Year', 'Date', 'YTM_rd'])
for i in bootstraping_rd.index:
    bootstraping_rd.iloc[i, 0] = i + 1
    bootstraping_rd.iloc[i, 1] = issue_date + relativedelta(years=i+1)

for i in bootstraping_rd.index:
    for j in YTM.index:
        if bootstraping_rd.loc[i, 'Year'] == YTM.loc[j, 'Month']/12:
            bootstraping_rd.loc[i, 'YTM_rd'] = YTM.loc[j, 'YTM_rd']

for i in bootstraping_rd.index:
    if bootstraping_rd.loc[i, 'YTM_rd'] == 0:
        j = 1
        while bootstraping_rd.loc[i + j, 'YTM_rd'] == 0:
            j = j + 1
            if bootstraping_rd.loc[i + j, 'YTM_rd'] > 0:
                break
        bootstraping_rd.loc[i, 'YTM_rd'] = bootstraping_rd.loc[i - 1, 'YTM_rd'] + (bootstraping_rd.loc[i + j, 'YTM_rd'] \
            - bootstraping_rd.loc[i - 1, 'YTM_rd'])/ (j+1)

bootstraping_rd['spot_rd'] = 0
bootstraping_rd['coupon_rd'] = bootstraping_rd['YTM_rd']
bootstraping_rd['DFPVC_rd'] = 0
bootstraping_rd['LP_rd'] = bootstraping_rd['coupon_rd'] + 1
bootstraping_rd['PVC_rd'] = 0
bootstraping_rd['PYLP_rd'] = 0
bootstraping_rd.loc[0, 'spot_rd'] = bootstraping_rd.loc[0, 'YTM_rd']
bootstraping_rd.loc[0, 'PVLP_rd'] = 1

for i in bootstraping_rd.index:
    if i >= 1:
        bootstraping_rd.loc[i, 'DFPVC_rd'] = bootstraping_rd.loc[ i - 1, 'DFPVC_rd'] + (1/(1 + bootstraping_rd.loc[ i-1, 'spot_rd'])) \
            ** bootstraping_rd. loc[i-1, 'Year']
        bootstraping_rd.loc[i, 'PVC_rd'] = bootstraping_rd.loc[i, 'coupon_rd'] * bootstraping_rd.loc[i, 'DFPVC_rd']
        bootstraping_rd.loc[i, 'PVLP_rd'] = 1 - bootstraping_rd.loc[i, "PVC_rd"]
        bootstraping_rd.loc[i, 'spot_rd'] = (bootstraping_rd.loc[i, 'LP_rd'] / bootstraping_rd. loc[i, 'PVLP_rd']) **\
             (1 / bootstraping_rd.loc[i, 'Year']) - 1


# 선형보간법 적용
dt_ind = pd.date_range(start = issue_date, end = maturity_date)
cols = [
'rf_spotrate', 'rf_spotrate_pv', 'rf_spotrate_pv_Shift', 'rf_forwardrate_pv_node', 'rf_forwardrate',
'rd_spotrate', 'rd_spotrate_pv', 'rd_spotrate_pv_Shift', 'rd_forwardrate_pv_node',  'rd_forwardrate'
]

YTM_linear = pd.DataFrame(np.NaN, dt_ind, cols)

for i in YTM_linear.index:
    itime = i.strftime('%Y-%m-%d')
    for j in YTM.index:
        if itime == (issue_date + relativedelta(months = YTM.loc[j, 'Month'])).strftime('%Y-%m-%d'):
            YTM_linear.loc[i, 'rf_spotrate'] = YTM.loc[j, 'YTM_rf']
            YTM_linear.loc[i, 'rd_spotrate'] = YTM.loc[j, 'YTM_rd']

for i in YTM_linear.index:
    itime = i.strftime('%Y-%m-%d')
    for j in bootstraping_rf.index:
        if itime == (issue_date + relativedelta(years = j + 1)).strftime('%Y-%m-%d'):
            YTM_linear.loc[i, 'rf_spotrate'] = bootstraping_rf.loc[j, 'spot_rf']


for i in YTM_linear.index:
    itime = i.strftime('%Y-%m-%d')
    for j in bootstraping_rd.index:
        if itime == (issue_date + relativedelta(years = j + 1)).strftime('%Y-%m-%d'):
            YTM_linear.loc[i, 'rd_spotrate'] = bootstraping_rd.loc[j, 'spot_rd']

YTM_linear = YTM_linear.interpolate(method='time')

YTM_linear = YTM_linear.fillna(method='bfill')




#forwardrate 계산
for i in YTM_linear.index:
    if i.date() == issue_date:
        YTM_linear.loc[i, 'rf_spotrate_pv'] = (1 / (1+YTM_linear.loc[ i, 'rf_spotrate'])) ** (1 / 365)
        YTM_linear.loc[i, 'rf_forwardrate_pv_node'] = YTM_linear.loc[ i, 'rf_spotrate_pv']
        YTM_linear.loc[i, 'rf_forwardrate'] = ((1 / YTM_linear.loc[ i, 'rf_spotrate_pv']) ** 365) - 1

        YTM_linear.loc[i, 'rd_spotrate_pv'] = (1 / (1+YTM_linear.loc[ i, 'rd_spotrate'])) ** (1 / 365)
        YTM_linear.loc[i, 'rd_forwardrate_pv_node'] = YTM_linear.loc[ i, 'rd_spotrate_pv']
        YTM_linear.loc[i, 'rd_forwardrate'] = ((1 / YTM_linear.loc[ i, 'rd_spotrate_pv']) ** 365) - 1



    else:
        YTM_linear.loc[i, 'rf_spotrate_pv'] = (1 /(1+ YTM_linear.loc[ i, 'rf_spotrate'])) ** (((i.date() - issue_date).days + 1) / 365)
        YTM_linear['rf_spotrate_pv_Shift'] = YTM_linear['rf_spotrate_pv'].shift(1, fill_value=0)
        YTM_linear.loc[i, 'rf_forwardrate_pv_node'] = YTM_linear.loc[ i, 'rf_spotrate_pv'] / YTM_linear.loc[ i, 'rf_spotrate_pv_Shift']
        YTM_linear.loc[i, 'rf_forwardrate'] = ((1 / YTM_linear.loc[ i, 'rf_forwardrate_pv_node']) ** 365) - 1

        YTM_linear.loc[i, 'rd_spotrate_pv'] = (1 /(1+ YTM_linear.loc[ i, 'rd_spotrate'])) ** (((i.date() - issue_date).days + 1) / 365)
        YTM_linear['rd_spotrate_pv_Shift'] = YTM_linear['rd_spotrate_pv'].shift(1, fill_value=0)
        YTM_linear.loc[i, 'rd_forwardrate_pv_node'] = YTM_linear.loc[ i, 'rd_spotrate_pv'] / YTM_linear.loc[ i, 'rd_spotrate_pv_Shift']
        YTM_linear.loc[i, 'rd_forwardrate'] = ((1 / YTM_linear.loc[ i, 'rd_forwardrate_pv_node']) ** 365) - 1



YTM_linear.to_excel('inventors.xlsx')


