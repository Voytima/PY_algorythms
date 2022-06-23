# 9) Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)..

"""Надо проверить двойные неравенства чисел, а так же равенство двух или трех чисел"""


def mid_num(a, b, c):
    if a == b or b == c or a == c or a == b == c:
        return f'Среднего числа нет т.к. 2 или 3 числа равны между собой'
    elif b < a < c or c < a < b:
        return f'Среднее число: {a}'
    elif a < b < c or c < b < a:
        return f'Среднее число: {b}'
    else:
        return f'Среднее число: {c}'


if __name__ == '__main__':
    print(
        mid_num(
            int(input('Enter first num: ')),
            int(input('Enter second num: ')),
            int(input('Enter third num: '))
        )
    )


