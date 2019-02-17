#! -*- coding:utf-8 -*-
import pandas as pd

def data_clean():
    data = pd.read_excel('ClimateChange.xlsx',sheetname=0)
    data = data[data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')
    data.drop(labels=['Country name','Series code','Series name','SCALE','Decimals'],axis=1,inplace=True)
    data.replace({'..':pd.np.nan},inplace=True)
    data = data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    data.dropna(how='all',inplace=True)
    data['Sum emissions'] = data.sum(axis=1)
    data1=pd.DataFrame()
    data1 = data['Sum emissions']

    country = pd.read_excel('ClimateChange.xlsx',sheetname=1)
    country.set_index('Country code')
    country.drop(labels=['Capital city','Region','Lending category'],axis=1,inplace=True)
    country.set_index('Country code')

    return pd.concat([data1,country],axis=1)

def co2():
    df = data_clean()
    df_sum = df.groupby('Income group').sum()
    
    df_max = df.sort_values(by='Sum emissions',ascending=False).groupby('Income groups').head(1).set_index('Income group')
    df_max.columns = ['Highest emission country','Highest emissions']
    df_max = df_max.reindex(columns = ['Highest emission country','Highest emissions'])

    df_min = df.sort_values(by='Sum emissions').groupby('Income groups').head(1).set_index('Income group')
    df_min.columns = ['Highest emission country','Highest emissions']
    df_max = df_min.reindex(columns = ['Highest emission country','Highest emissions'])

    results = pd.concat([df_sum,df_max,df_min],axis=1)
    return result

