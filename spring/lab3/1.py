"""В файле melting.txt приведены значения флуоресценции различных образцовв диапазоне температур от 28 до 95 градусов.
   Сами эти абсолютные значения  не слишком интересуют исследователей: важнее форма кривых.  Чтобы было удобнее сравнивать
   кривые между собой, отнормируйте их (минимальное значение - 0, максимальное - 1, промежуточное значение делится на разницу
   между максимальным и минимальным значением). Постройте графики получившихся кривых."""
import numpy as np
import matplotlib.pyplot as plt
temp, col1,col2,col3,col4,col5 = np.loadtxt('melting.txt',skiprows=1,usecols=(0,1,2,3,4,5),unpack=True)
def redone(col):
   mmin=np.min(col)
   mmax=np.max(col)
   for i in range(len(col)):
    if col[i]==mmin:
     col[i]=0
    if col[i]==mmax:
        col[i]=1
    else:
       col[i]= (col[i]-mmin)/(mmax-mmin)
redone(col1)
redone(col2)
redone(col3)
redone(col4)
redone(col5)
def graph(col):
 plt.plot(temp,col)
 plt.xlabel('time')
 plt.ylabel('detector signal')
graph(col1)
graph(col2)
graph(col3)
graph(col4)
graph(col5)
plt.show()
