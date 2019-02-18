import pandas as pd

def co2():
    data = pd.read_excel('ClimateChange.xlsx')
    data = data[data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')
    data.drop(data.columns[:5], axis=1, inplace=True)
    data.replace({'..':pd.np.nan},inplace=True)
    data = data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    country = pd.read_excel('ClimateChange.xlsx', 1).set_index('Country code')
    df = pd.concat([data.sum(1), country['Income group']], 1)
    a = df.groupby('Income group').sum()
    a.columns = ['Sum emissions']
    df[2] = country['Country name']
    df_max = df.sort_values(0, 
        ascending=False).groupby('Income group').head(1).set_index('Income group')
    df_max.columns = ['Highest emissions','Highest emission coutry']
    df_min = df[df[0]>0].sort_values(0).groupby('Income group'\
        ).head(1).set_index('Income group')
    df_min.columns = ['Lowest emissions', 'Lowest emission country']
    results =  pd.concat([a, df_max, df_min], 1)
    results = results[['Sum emissions','Highest emission coutry','Highest emissions', 'Lowest emission country','Lowest emissions']]
    return results

if __name__ == '__main__':
    print(co2())
