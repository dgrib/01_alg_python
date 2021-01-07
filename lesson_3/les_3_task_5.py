"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""
from random import randint

array = [randint(-20, 20) for _ in range(20)]
print(array)

max_negative = 20
for elem in array:
    if elem < 0 and abs(elem) < max_negative:
        max_negative = abs(elem)


print(f'Максимальный отрицательный элемент {max_negative*-1}, его позиция в массиве {array.index(max_negative*-1) + 1}')
print('\nПримечание: отсчет позиции начинается с 1, программа выдает позицию первого появления элемента.')
