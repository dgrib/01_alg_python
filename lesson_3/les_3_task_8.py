"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
matrix_range = 4
matrix = [[0] * matrix_range for _ in range(matrix_range)]

print('Вводите элементы матрицы 4х4 поочередно (неотрицательные числа): ')

for line in range(matrix_range):
    line_sum = 0
    for elem in range(matrix_range):
        while True:
            user_num = input(f'Введите {elem + 1} элемент {line + 1} строки матрицы: ')
            if user_num.isdigit():
                break
        matrix[line][elem] = int(user_num)
        line_sum += matrix[line][elem]
    matrix[line].append(line_sum)

# вывод матрицы
for line in matrix:
    for elem in line:
        print(f'{elem:>5}', end='')
    print()

