"""В файле chromo.txt находится хроматограмма - сигнал детектора
   в зависимости от времени.Продемонстрируйте данные на графике.
   Столбцы разделены табуляцией - \t.
   Разрешается (и приветствуется) просмотр исходных файлов."""

import numpy as np
import matplotlib.pyplot as plt
time, value = np.loadtxt('chromo.txt',skiprows=1,unpack=True)
plt.plot(time,value)
plt.xlabel('time')
plt.ylabel('detector signal')
plt.show()
