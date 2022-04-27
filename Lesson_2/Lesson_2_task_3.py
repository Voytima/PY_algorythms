# 3) Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

"""Тут пришлось немного подумать как реализовать. Смысл в том, чтобы вводимое число поделить на 10,
чтобы отщепить последнюю цифру. Далее взять эту цифру (остаток от деления) и добавить к перевертышу в конец.
Как добавить в конец перевертыша правильно? Надо число сдвинуть в разряде. Например, число 153. 3 + 5 + 1 = 9 - неверно.
А если сдвинем разрядности, то получится как надо: (3*10 + 5) * 10 + 1 = 351"""


def revert(i):
    k = 0
    while i > 0:
        k = k * 10 + i % 10
        i //= 10
    return f'Your revert number is {k}'


if __name__ == '__main__':
    print(
        revert(
            int(input('Enter any number to revert: '))
        )
    )
