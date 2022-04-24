# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def sum_mult(number):
    summ = 0
    mult = 1
    if number == 0:
        mult = 0
    while number > 0:
        rest_num = number % 10
        if rest_num != 0:
            summ += rest_num
            mult *= rest_num
        number //= 10
        if rest_num == 0:
            mult = 0
    # if number == 0:
    #     mult = 0
    return f'Сумма чисел: {summ}\nПроизведение чисел: {mult}'


if __name__ == '__main__':
    print(
        sum_mult(
            abs(int(input('Введите трехзначное число: '))
            ))
     )
