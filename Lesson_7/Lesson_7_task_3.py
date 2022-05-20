# 3) Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from random import randint


def median(nums, med):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    pivot = nums[0]
    bigger = []
    lesser = []
    pivots = []

    for i in nums:
        if i < pivot:
            lesser.append(i)
        elif i > pivot:
            bigger.append(i)
        else:
            pivots.append(i)
    # print(f'LESSER {lesser}')
    # print(f'BIGGER {bigger}')
    # print(f'PIVOTS {pivots}')

    if len(lesser) > med:
        return median(lesser, med)
    elif len(lesser) + len(pivots) > med:
        return pivots[0]
    else:
        return median(bigger, med - len(bigger) - len(pivots))


if __name__ == '__main__':
    n = int(input('How many numbers: '))
    num = [randint(-100, 100) for x in range(2 * n + 1)]

    print(f'Source list: {num}')
    print(f'Median: {median(num, n)}')
