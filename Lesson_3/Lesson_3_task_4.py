# 4) Определить, какое число в массиве встречается чаще всего.

from random import random
"""Создаем массив на размер заданный пользователем"""
n = int(input('Enter a number of numbers: '))
a = [0] * n
for i in range(n):
    a[i] = int(random() * 11)
print(f'The array for search is: {a}')

common_num = a[0]   # Это самая встречающаяся цифра
how_often = 1       # Это счетчик этой цифры

"""Сравнивать будем первую цифру и следующую за ней до предпоследней т.к. последнюю не с чем сравнивать"""
for i in range(n - 1):
    case = 1        # Вводим счетчик цифры, который равен 1 т.к. 1 раз мы уже встретили цифру на первой позиции
    for j in range(i + 1, n):
        if a[i] == a[j]:    # При совпадении цифр
            case += 1       # увеличиваем счетчик на 1
        if case > how_often:    # и присваиваем переменным обновленные значения
            how_often = case
            common_num = a[i]
if how_often > 1:
    print(f'Number |{common_num}| is the most common in array with frequency {how_often}')
else:
    print(f'WOW! In array {a} all elements are unique!')
