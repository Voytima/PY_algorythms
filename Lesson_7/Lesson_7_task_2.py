# 2) Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50]. Выведите на экран исходный и отсортированный массивы
from random import randint


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [j for j in nums[1:] if j <= pivot]
        greater = [j for j in nums[1:] if j > pivot]
        return merge_sort(less) + [pivot] + merge_sort(greater)


if __name__ == '__main__':
    n = int(input('How many numbers: '))
    num = [randint(0, 50) for x in range(n)]

    print(f'Source list: {num}')
    print(f'Sorted list: {merge_sort(num)}')

"""
Мне кажется, что метод C&C подходит, ведь там тоже идет как бы слияние массивов. Но, есть еще один вариант
длинее со слиянием-слиянием.
"""
# 2


def merge_array(start, end):
    merged = []
    while len(start) or len(end):
        if len(start) and len(end):
            merged.append(start.pop(0) if start[0] < end[0] else end.pop(0))
        else:
            merged.append(start.pop(0) if len(start) else end.pop(0))
    return merged


def merge_sort_2(nums_2):
    if len(nums_2) <= 2:
        return nums_2 if len(nums_2) == 1 or nums_2[0] < nums_2[1] else [nums_2[1], nums_2[0]]
    mid = len(nums_2) // 2
    return merge_array(merge_sort_2(nums_2[:mid]), merge_sort_2(nums_2[mid:]))


if __name__ == '__main__':
    n = int(input('How many numbers: '))
    num = [randint(0, 50) for x in range(n)]

    print(f'Source list: {num}')
    print(f'Sorted lists:\n Two_func: {merge_sort_2(num)}\n Com&Conq: {merge_sort(num)}')
