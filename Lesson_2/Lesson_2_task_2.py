# 2) Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def counter(i):
    if i <= 0:
        print('Make no sense, zero is zero')
    else:
        chet = 0
        ne_chet = 0
        while i > 0:
            if i % 2 == 0:
                chet += 1
            else:
                ne_chet += 1
            i //= 10
        return f'In number you entered chet = {chet}, ne_chet = {ne_chet}'


if __name__ == '__main__':
    print(
        counter(
            int(input('Enter any natural number: '))
        )
    )
