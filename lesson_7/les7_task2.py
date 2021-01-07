# -*- coding: utf-8 -*-
"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""


def merge_sort(data):
    """
    Рекурсивная версия сортировки слиянием. Само слияние вынесено в отдельную функцию
    :param data: list
    :return: sorted list
    """
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        if i < len(left):
            result.extend(left[i:])
        elif j < len(right):
            result.extend(right[j:])
        return result

    count = len(data)
    middle = count // 2
    if count > 2:
        part_1 = merge_sort(data[:middle])
        part_2 = merge_sort(data[middle:])
        return merge(part_1, part_2)

    elif count > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data


if __name__ == '__main__':
    import random
    numbers = 11
    some_list = [random.random()*50 for _ in range(numbers)]
    print(some_list)
    print(merge_sort(some_list))
