# -*- coding:utf-8 -*-
import pandas as pd
apple = 'http://labfile.oss.aliyuncs.com/courses/764/apple.csv'
def quarter_volume():
    data = pd.read_csv(apple,header=0)
    i=pd.to_datetime(data['Date'])
    data1 = pd.Series(list(data['Volume']),index=i)
    volume = list(data1.resample('Q').sum())
    second_volume = sorted(volume)[-2]
    print(second_volume)
    return second_volume

if __name__ == '__main__':
    quarter_volume()
    
