# 7) Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def example(i):
    x = i * (i + 1) // 2
    k = 0
    for i in range(1, i + 1):
        k += i
    return f'left part *{k}* is equal to right part *{x}*'


if __name__ == '__main__':
    print(
        example(
            int(input('Enter any natural number: '))
        )
    )




