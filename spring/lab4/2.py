"""Прочитайте данные из файла Cell_culture.txt о количестве суспензионной культуры,
   заказанной сотрудниками и студентами лаборатории на определённые даты, в структурированный массив.
   Выведите на экран:

   суммарное количество культуры, заказанной на 5 апреля;
   имена студентов и сотрудников, которые заказали культуру на 9 апреля"""
import numpy as np
data=np.genfromtxt('Cell_culture.txt',skip_header=1,dtype=[('date','U10'),('name','U10'),('volume','f8'),('comment','U10')])
x=data[0]
print(x)
s=0
for i in data:
        if i[0]=='5-Apr':
           s+=int(i[2])
        else:
            continue
print('the amount of culture booked on 5-Apr is ',s)
ss=[]
for i in data:
        if i[0]=='9-Apr':
         ss.append(i[1])
        else:
            continue
print('names of students who ordered culture on 9-Apr are ',ss)





