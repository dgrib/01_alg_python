"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint

min_value = 1
max_value = 50
matrix_range = 5

# формируем матрицу из случайных элементов
matrix = [[randint(min_value, max_value) for _ in range(matrix_range)] for _ in range(matrix_range)]
# формируем список минимальных элементов каждого столбца
min_list = [50] * matrix_range

# выводим матрицу на печать и заодно заполняем список минимальных элементов каждого столбца
for line in matrix:
    for pos, elem in enumerate(line):
        if elem < min_list[pos]:
            min_list[pos] = elem
        print(f'{elem:>5}', end='')
    print()

print('*' * 30)

# выводим на печать список мин элементов столбцов и заодно ищем среди них максимальный
max_among_min = min_value
for elem in min_list:
    if elem > max_among_min:
        max_among_min = elem
    print(f'{elem:>5}', end='')

print('    мин значения из элементов столбца')
print(f'\n{max_among_min} максимальное значение из минимальных элементов столбцов.')


