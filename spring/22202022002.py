"""открыть,добычть числовые данные, построить от 4 до 7,
   отриц знач не было, мин - 0. Найти самую высокую точку,
   распаковать в отдельную папку."""
import pandas as pd
import numpy as np
import os

getway=r'C:\Users\anast\Desktop\лабы по питоне\сдача\files'
where_files = os.listdir(getway)

for file in where_files:
    way, file_type = os.path.splitext(file,)
    if file_type == '.csv':
        df = pd.read_csv(file)
        col=df[2]
        mmin = np.min(col)
        mmax = np.max(col)
        for i in range(len(col)):
            if col[i] == mmin:
                col[i] = 0
            if col[i]<=0:
                col[i]==0
        df.plot(df.columns[0], df.columns[2], title = 'Data (4-7 min)')
