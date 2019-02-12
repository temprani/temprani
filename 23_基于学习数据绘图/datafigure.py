import pandas as pd
from matplotlib import pyplot as plt

def data_plot():
    filepath = 'http://labfile.oss.aliyuncs.com/courses/764/user_study.json'
    data = pd.read_json(filepath,orient='values',encoding='utf-8')
    df = data.groupby('user_id').sum()
    ax = df.plot.line(title='StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    plt.show()
    return ax

if __name__ == '__main__':
    data_plot()
    '''
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    y = df2['minutes']
    x = df2.index 
    ax.plot(x, y)

    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')

    #ax.set_xticks(np.arange(0,200000,50000))
    #ax.set_yticks(np.arange(0,3000,500))
    '''
