import pandas as pd
def data_clean():
    data = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    data = data[data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')
    data.drop(labels=['Country name','Series code','Series name','SCALE','Decimals'],axis=1,inplace=True)
    data.replace({'..':pd.np.nan},inplace=True)
    data = data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    data.dropna(how='all',inplace=True)
    data['Sum emissions'] = data.sum(axis=1)
    data = data['Sum emissions']

    df_hc =df_sum2.sort_values(by='Sum emission',ascending=False).groupby('Income group').head(1).set_index(Income group)

