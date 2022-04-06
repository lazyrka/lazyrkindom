import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 5))
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

x=reading_1_column('chromo.txt')
y1=reading_2_column('chromo.txt')
plt.plot(x, y1)


plt.title('Показания детектора')
plt.xlabel('время')
plt.ylabel('показания')
plt.show()