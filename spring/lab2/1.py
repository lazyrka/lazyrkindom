"""В файлах wild_type.txt и mutant.txt находятся данные по флуоресценции клеток,
   экспрессирующих обычную и мутантную формы белка, соответственно,
   в зависимости от концентрации лиганда (вещества, которое взаимодействует с белком).
   Продемонстрируйте данные на графике. Столбцы разделены табуляцией - \t.
   Разрешается (и приветствуется) просмотр исходных файлов."""
import numpy as np
import matplotlib.pyplot as plt
col1, col2_mut= np.loadtxt('mutant.txt', usecols=(0, 1),skiprows=1, unpack=True)
col2_wild=  np.loadtxt('wild_type.txt', usecols=(1),skiprows=1, unpack=True)
plt.scatter(col1, col2_wild, label='wild type')
plt.scatter(col1, col2_mut, label='mutant')
plt.title('Флуоресценция')
plt.xlabel('Белок')
plt.ylabel('Отклик')
plt.legend(loc='best', fontsize=9)
plt.show()
