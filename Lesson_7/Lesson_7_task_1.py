# 1) Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100]. Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint


def bubble_sort(nums):
    print(f'Source list {nums}')
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    n = int(input('How many numbers: '))
    s = [0] * n
    for k in range(n):
        s[k] = randint(-100, 100)
    print(f'Sorted list {bubble_sort(s)}')
