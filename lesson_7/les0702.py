"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
from random import randint


def fusion_sort(array):
    if len(array) < 2:
        return array
    elif len(array) > 1:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]

        left = fusion_sort(left)
        right = fusion_sort(right)

        result = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            # <= дает устойчивость, сохраняет порядок равных элементов
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1

            else:
                result.append(right[right_index])
                right_index += 1

        result += left[left_index:]
        result += right[right_index:]
        return result


size = 10
array = [randint(0, 49) for i in range(size)]
print(f'{array} - несортированный список')
print(f'{fusion_sort(array)} - сортированный список')
