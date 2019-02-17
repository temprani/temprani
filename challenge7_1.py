#! -*- coding:utf-8 -*-
import pandas as pd
def co2():
    #文件提取
    url='http://labfile.oss.aliyuncs.com/courses/1013/week7/ClimateChange.xlsx'
    data=pd.read_excel(url,sheetname=0)
    country=pd.read_excel(url,sheetname=1)
    country.set_index('Country code')
    #data文件清洗
    data=data[data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')
    data.replace({'..':pd.np.nan},inplace=True)
    data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    year=list(range(1990,2012))
    data.dropna(how='all',inplace=True)

    #文件合并，计算1990～2011总排量，删除0
    df_climate = pd.merge(data,country)
    df_climate['sum']=df_climate.loc[:,year].sum(axis=1)
    
    df_sum1=df_climate[df_climate['sum']>0]
    df_sum2=pd.DataFrame(df_sum1.loc[:,['Country name','Income group','sum']])
    df_sum2.set_index('Country name')
    #分组计算
    results=pd.DataFrame()
    results['Sum emissions'] = df_sum2.groupby('Income group').sum(axis=1)['sum']
    results['Highest emission country'] = df_sum2.groupby('Income group').max(axis=1)['Country name']
    results['Highest emissions'] = df_sum2.groupby('Income group').max(axis=1)['sum']
    results['Lowest emission country']=df_sum2.groupby('Income group').min(axis=1)['Country name']
    results['Lowest emissions']=df_sum2.groupby('Income group').min(axis=1)['sum']
    return results

if __name__ == '__main__':
    print(co2())
