# 3) В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

n = int(input('Введите количество чисел: '))
a = [0] * n     # Создаем массив от 0 до n

for i in range(n):
    a[i] = int(random() * 21)   # Заполняем случайными числами, например от 0 до 20
    print(a[i], end=' ')
"""Теперь будем искать мин и макс число. Мне кажется, что удобнее будет работать с индексами чисел"""
min_num = min(a)    # Минимальное число в массиве n
max_num = max(a)    # Максимальное число в массиве n
min_num_idx = a.index(min_num)  # Индекс минимального числа
max_num_idx = a.index(max_num)  # Индекс максимального числа

print()
print(f'Min_number is: |{min(a)}| index: |{min_num_idx + 1}|')
print(f'Max_number is: |{max(a)}| index: |{max_num_idx + 1}|')

a[min_num_idx], a[max_num_idx] = a[max_num_idx], a[min_num_idx]     # Меняем макс и мин индексы местами

for i in range(n):      # Финальный принт
    print(a[i], end=' ')



