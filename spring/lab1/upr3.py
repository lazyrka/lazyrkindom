import matplotlib.pyplot as plt

def krug(a,b,c,d,f):
 a1=(a/(a+b+c+d+f))*100
 a2=(b/(a+b+c+d+f))*100
 a3=(c/(a+b+c+d+f))*100
 a4=(d/(a+b+c+d+f))*100
 a5=(f/(a+b+c+d+f))*100
 data = [a1, a2, a3,a4, a5]
 plt.title('Название', size=14)
 plt.pie(data, labels=('Класс 1', 'Класс 2', 'Класс 3', 'Класс 4', 'Класс 5'))
 plt.show()
krug(16,18,20,22,24)
krug(20,20,18,22,20)
krug(24,22,20,18,16)