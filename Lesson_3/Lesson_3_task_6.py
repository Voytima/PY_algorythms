# 6) В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random

""" Создаем массив размера n"""
n = int(input('The array length is: '))
a = [0] * n
for i in range(n):
    a[i] = int(random() * 21)
print(f'The array is: {a}')

min_num = 0     # Индекс минимального значения в массиве
max_num = 0     # Индекс максимального значения в массиве

"""Перебираем массив от 0 до n. При нахождении наименьшего и наибольшего значений - запоминаем их"""
for i in range(0, n):
    if a[i] < a[min_num]:
        min_num = i
    elif a[i] > a[max_num]:
        max_num = i
print(f'Minimal number is |{a[min_num]}|, maximal number is |{a[max_num]}|')

if min_num > max_num:   # Если индекс меньшего значения больше большего - меняем их местами
    min_num, max_num = max_num, min_num

num_sum = 0     # Переменная для подсчета суммы элементов массива

"""Перебираем массив от мин+1 (т.к. не включительно должно быть) до макс и суммируем значения"""
for i in range(min_num + 1, max_num):
    num_sum += a[i]
print(f'The sum of elements between min and max is |{num_sum}|')
