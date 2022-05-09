"""Напишите функцию, которая печатает среднеквадратичное отклонение
   и межквартильный размах непустого упорядоченного списка,
   и продемонстрируйте её корректность ее работы"""
import numpy as np
print('input numbers that should be put in list')
num=input()
a=list()
while num!='':
 a.append(int(num))
 num=input()
a.sort()
print(a)

print('standard deviation of this list is ', np.std(a))
print('interquartile range of this list is ', np.percentile(a, 75,) - np.percentile(a, 25))
