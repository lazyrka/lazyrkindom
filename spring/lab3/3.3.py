"""Задан двумерный массив:

    square = np.array([ [16, 3, 2, 13],
                      [5, 10, 11, 8],
                      [9, 6, 7, 12],
                      [4, 15, 14, 1]])
    Вычислите сумму чисел в каждом столбце, в каждой строке, в каждом квадрате 2×2,
    который можно вырезать из имеющегося (5 шт). Выведите её на экран для каждого случая."""
import numpy as np
Array=np.array([ [16, 3, 2, 13], [5, 10, 11, 8],[9, 6, 7, 12],[4, 15, 14, 1]])
rows,cols =Array.shape
sum_rows=[]
def sum_cols_and_rows(array):
 a = 0
 ss=0
 for i in range(rows): #function that calculated sum of row and column elements
    aa=array[i,:]
    for j in range(cols):
        ss+=aa[j]
    sum_rows.append(ss)
    ss=0
 print('sum of raws or columns is ',sum_rows)
 sum_rows.clear()
TArray=Array.transpose()
sum_cols_and_rows(Array)
sum_cols_and_rows(TArray)
sq1=Array[0:2,0:2]
sq2=Array[0:2,2:4]
sq3=Array[2:4,0:2]
sq4=Array[2:4,2:4]
sq5=Array[1:3,1:3]

def sum_all_el(array):
    x=0
    for i in range(2):
     for j in range(2):
         x+=int(array[i,j])
    print(x)
    x=0
sum_all_el(sq1)
sum_all_el(sq2)
sum_all_el(sq3)
sum_all_el(sq4)
sum_all_el(sq5)




