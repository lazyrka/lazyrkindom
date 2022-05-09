"""В президентских выборах участвовало 5 кандидатов: А., Б., В., Г., Д.
   Социологическая служба провела опрос за месяц до выборов, за неделю
   до выборов и экзит-полл.

     Опрос	А.	Б.	В.	Г.	Д.
      #1	16	18	20	22	24
      #2	20	20	18	22	20
      #3	24	22	20	18	16
   Постройте круговые и столбчатые диаграммы результатов опросов.
   В комментариях к коду напишите, какие диаграммы показались Вам более наглядными."""
import numpy as np
import matplotlib.pyplot as plt
month=np.array([16,18,20,22,24])
week=np.array([20,20,18,22,20])
exit_poll=np.array([24,22,20,18,16])
names=np.array(['А.','Б.','В.','Г.','Д'])
#pie chart
def pie(x):
 plt.pie(x, labels=('А.', 'Б.', 'В.', 'Г.', 'Д.'))
 plt.show()
pie(month)
pie(week)
pie(exit_poll)
#bar chart seems to me more significant
def bar(x):
 plt.bar(names, x, edgecolor='k')
 plt.grid(True, axis='y')
 plt.show()
bar(month)
bar(week)
bar(exit_poll)