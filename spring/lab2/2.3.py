import math as m
import numpy as np

def reading_x (name):
    f=open(name, 'r')
    Flag=True
    x=[]
    for line in f:
        if Flag==False:
            a=line.split()
            x.append(float(a[0]))
        Flag=False
    f.close()
    return x

def reading_y (name):
    f=open(name, 'r')
    Flag=True
    y=[]
    for line in f:
        if Flag==False:
            a=line.split()
            y.append(float(a[1]))
        Flag=False
    f.close()
    return y
def correlation (x,y):
    dsx= np.std(x)
    dsy= np.std(y)
    n=len(x)
    a=[]
    for i in range (n):
        element=((x[i]-np.mean(x))/dsx)*((y[i]-np.mean(y))/dsy)
        a.append(element)
    S=np.sum(a)
    r=1/n*S
    return r

x1=reading_x('mutant.txt')
y11=reading_y('mutant.txt')
y12=reading_y('wild_type.txt')

x01 = [1, 2, 3, 4, 5]
y01 = [0.99, 0.49, 0.35, 0.253, 0.18]
x02 = np.random.rand(100)
y02 = np.random.rand(100)

data = 10 * np.random.rand(100) 
x03 = np.sort(data)
epsilon3 = np.random.rand(100)
y03 = (x03-5)**2 / 10 + epsilon3 - 0.5

r11=correlation(x1,y11)
r12=correlation(x1,y12)

r01=correlation(x01,y01)
r02=correlation(x02,y02)
r03=correlation(x03,y03)
print('mutant: r =', r11)
print('wild_type: r =', r12)

print('малое количество точек: r =', r01)
print('переменные не связаны между собой: r =', r02)
print('переменная: r =', r03)