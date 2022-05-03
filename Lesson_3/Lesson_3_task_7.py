# 7) В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться

from random import random

"""Тут можно решить простым путем через функции min и remove"""

n = int(input('The array length is: '))
a = [0] * n
for i in range(n):
    a[i] = int(random() * 21)
print(f'The array is: {a}')

min_num_1 = min(a)
a.remove(min_num_1)
min_num_2 = min(a)
print(f'First min_num is |{min_num_1}| and second min_num is |{min_num_2}|')
