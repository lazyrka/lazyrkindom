"""Вычислите среднее и стандартное отклонение чисел из файла ex4.txt,
   затем найдите выбросы (x < Q1 - 1.5 × IQR или x > Q3 + 1.5 × IQR
   и вычислите среднее и стандартное отклонение без них."""
import numpy as np

ex4=np.loadtxt('ex4.txt',unpack=True)
a=ex4.std()
print('standard deviation is ', a)
b=np.mean(ex4)
print('average deviation is ', b)
ex4.sort()
x = [i for i in np.quantile(ex4, [0.25,0.5,0.75])]
filenew = []
for i in ex4:
    if i > (x[0] - 1.5 * (x[2] - x[0])) and i < (x[2] + 1.5 * (x[2] - x[0])):
            filenew.append(i)
filenew1=np.array(filenew)
a1=filenew1.std()
b1=np.mean(filenew1)
print('new standard deviation is ', a1)
print('new average deviation is ', b1)


