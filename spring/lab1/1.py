"""Напишите функцию,
   которая возвращает медиану непустого упорядоченного списка,
   и продемонстрируйте её корректность её работы"""
import numpy as np
print('input numbers that should be put in list')
num=input()
a=list()
while num!='':
 a.append(int(num))
 num=input()
a.sort()
print(a)
print('median of this list is ', np.median(a))

