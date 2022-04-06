import matplotlib.pyplot as plt
import numpy as np

def reading_1_column (name):
    file=open(name, 'r')
    smena=True
    x=[]
    for line in file:
        if smena==False:
            a=line.split()
            x.append(float(a[0]))
        smena=False
    file.close()
    return x

def reading_2_column (name):
    file=open(name, 'r')
    smena=True
    y=[]
    for line in file:
        if smena==False:
            a=line.split()
            y.append(float(a[1]))
        smena=False
    file.close()
    return y

x=reading_1_column('mutant.txt')
y1=reading_2_column('mutant.txt')
y2=reading_2_column('wild_type.txt')

plt.scatter(x, y1, label='wild type')
plt.scatter(x, y2, label='mutant')
plt.title('Флуоресценция')
plt.xlabel('Белок')
plt.ylabel('Отклик')
plt.legend(loc='best', fontsize=9)
plt.show()