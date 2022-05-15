# 2) Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
from collections import deque

hex_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',   # список символов в 16-тиричном формате
               'A', 'B', 'C', 'D', 'E', 'F']

bin_nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,     # словарь перевода hex в bin
            '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def conversion(hex_num):    # Конвертация символов в верхний регистр и формирование очереди
    hex_deq = deque(hex_num.upper())
    return hex_deq


def num_sum(num_1, num_2):
    num_1 = num_1.copy()    # Создаем копии чтобы не изменились исходные данные
    num_2 = num_2.copy()

    if len(num_2) > len(num_1):
        num_1, num_2 = num_2, num_1     # Выбираем самую длинную переменную и ставим ее на 1 позицию

    num_2.extendleft('0' * (len(num_1) - len(num_2)))   # Добавить 0 чтобы не было ошибок при обращении к элементам

    res = deque()   # Очередь для реультатов
    v_yme = 0       # Если сумма будет больше 16 - принимает 1

    for i in range(len(num_1) - 1, - 1, - 1):   # попарное сложение цифр чисел
        first_num = bin_nums[num_1[i]]
        second_num = bin_nums[num_2[i]]
        result = first_num + second_num + v_yme

        if result >= 16:
            v_yme = 1
            result -= 16
        else:
            v_yme = 0

        res.appendleft(hex_nums[result])    # Расширяем очередь слева добавляя получившуюся цифру

    if v_yme == 1:  # Если есть 1, то ее дописываем
        res.appendleft('1')

    return res


def num_mult(num_1, num_2):
    num_1 = num_1.copy()    # Создаем копии чтобы не изменились исходные данные
    num_2 = num_2.copy()

    if len(num_2) > len(num_1):
        num_1, num_2 = num_2, num_1     # Выбираем самую длинную переменную и ставим ее на 1 позицию

    num_2.extendleft('0' * (len(num_1) - len(num_2)))   # Аналогично, если число_1 3 символа, а число_2-два,то добавим 0

    res = deque('0')   # Очередь для реультатов

    for i in range(len(num_1) - 1, - 1, - 1):   # Берем цифру второго числа
        second_num = bin_nums[num_2[i]]

        x = deque('0')  # Временная очередь

        """2*5 = 2+2+2+2+2. Это значит, что мы складываем цифру первого числа (2) n-раз (второе число(5))"""
        for j in range(second_num):     # Складываем два числа, которые хранится в (х и в num_1)*second_num раз
            x = num_sum(x, num_1)

        x.extend('0' * (len(num_1) - i - 1))    # восстанавливаем разрядность переменной х
        res = num_sum(res, x)

    return res


# Ввод данных (не зависит от регистра)
a = input('Enter first num in hex format (0-f): ')
b = input('Enter second num in hex format (0-f): ')

a = conversion(a)   # Конвертация из строки в элементы массива
b = conversion(b)   # Конвертация из строки в элементы массива

print('Sum: ', num_sum(a, b))
print('Mult: ', num_mult(a, b))
