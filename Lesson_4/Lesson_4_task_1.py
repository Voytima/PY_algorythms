# 1) a) Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
#    b) Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их


""" a)
Для примера разбора возьмем 8 задачу второго урока:
8) Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

import time

s = (int(input('Enter a number sequence: ')))   # последовательность цифр
n = (int(input('Enter a number to find in sequence: ')))    # какую цифру ищем
c = 0   # счетчик искомой цифры

start = time.time()

while s > 0:        # O(n)
    if s % 10 == n: # O(n)
        c += 1      # O(1)
    s //= 10        # O(1)

finish = time.time()

print(f'In sequence you entered the num |{n}| was found {c} time(-s)')
print(start)
print(finish)
print(f'{(finish - start):.10f}, sec')

"""
В данном алгоритме присутствует два цикла: ПОКА 's > 0' и ЕСЛИ 's % 10 == n'.
Получается O(n) и O(n). Итоговая сложность алгоритма O(n^2).
Для проверки скорости на моем ПК (для хоть какого-либо отображения времени выполнения) мне понадобилось взять число
1*10**300 и искомую цифру 1 (чтобы цикл прошел от конца к началу полностью) - худший случай.
"""

# b) Можно сравнить поиск числа обычным перебором и с помощью бинарного поиска
import time


def lin_search(lys, element):
    for i in range(len(lys)):
        if lys[i] == element:
            return i
    return -1


def binary_search(my_list, item):
    first = 0
    last = len(my_list) - 1
    index = -1

    while first <= last and index == -1:
        mid = (first + last) // 2
        if my_list[mid] == item:
            index = mid
        else:
            if item < my_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


to_find = 10000000

elements = [i for i in range(to_find + 1)]

start = time.time()
binary_search(elements, to_find)
end = time.time()
print(f'Binary_search_speed is: {(end - start):.10f} sec')

start = time.time()
lin_search(elements, to_find)
end = time.time()
print(f'Linear_search_speed is: {(end - start):.10f} sec')

"""Значения взяты из репла т.к. на моем пк почти всегда все значения нули:
For 10 elements:
Binary_search_speed is: 0.0000064 sec
Linear_search_speed is: 0.0000079 sec

For 100 elements:
Binary_search_speed is: 0.0000084 sec
Linear_search_speed is: 0.0000258 sec

For 1000 elements:
Binary_search_speed is: 0.0000167 sec
Linear_search_speed is: 0.0007222 sec

For 10000 elements:
Binary_search_speed is: 0.0000193 sec
Linear_search_speed is: 0.0425534 sec

For 100000 elements:
Binary_search_speed is: 0.0000327 sec
Linear_search_speed is: 0.0839140 sec

For 1000000 elements:
Binary_search_speed is: 0.0000365 sec
Linear_search_speed is: 0.6178970 sec

For 10000000 elements
Binary_search_speed is: 0.0000429 sec
Linear_search_speed is: 6.3693109 sec
"""

# Как видно из значений, при 10млн элементов Линейный поиск уже занимает секунды для поиска, в то время как
# бинарный поиск все еще находится на отметке 4.29 * 10(-5). Это подтверждает, что скорость алгоритма
# O (log n) работает в разы быстрее O(n) при увеличениее количества объема входных данных.
