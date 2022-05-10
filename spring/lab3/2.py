"""Прочитайте файлы ex2_1.txt и ex2_2.txt в двумерный массив,
   вычислите среднее по каждому столбцу. Читая файлы, исходите из предположения,
   что количество столбцов в файле заранее неизвестно. Числа в строке разделены табуляцией."""
import numpy as np
ex1=np.loadtxt('ex2_1.txt',unpack=True)
ex2=np.loadtxt('ex2_2.txt',unpack=True)
ex1_1=ex1.ravel()
ex2_2=ex2.ravel()
B=np.array([ex1_1,ex2_2], dtype=object) #two-dimensional array
middle_1=np.mean(ex1,axis=1)
middle_2=np.mean(ex2,axis=1)
print('the average value of the columns in the first facel is ',middle_1,' in the second - ', middle_2)



