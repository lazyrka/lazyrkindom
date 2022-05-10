"""Создайте квадратный массив (размером больше 2), отсортируйте его столбцы,
   получите транспонированный массив (от отсортированного), объедините эти массивы вертикально,
   горизонтально и без оси (выведите на экран результат для каждого действия)."""
import numpy as np
Array1= np.fromfunction(lambda i,j: 2*i*j, (4,4))
Array = np.sort(Array1, axis=0)
TArray=Array.transpose()
print('Array= ',Array,'\n TArray= ',TArray)
vertical=np.vstack((Array,TArray))
print('combining arrays vertically \n ', vertical)
horizontal= np.hstack((Array,TArray))
print('combining arrays horizontally \n ', horizontal)
without=np.concatenate((Array, TArray), axis=None)
print('combining arrays without axis \n ', without)