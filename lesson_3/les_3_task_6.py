"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
# from s


from random import randint

array = [randint(1, 30) for _ in range(10)]
print(array)

max_pos = 0
min_pos = 0

for pos in range(len(array)):
    if array[pos] > array[max_pos]:
        max_pos = pos
    if array[pos] < array[min_pos]:
        min_pos = pos

# меняем местами если позиция max < позиции min
if array[max_pos] < array[min_pos]:
    max_pos, min_pos = min_pos, max_pos

elem_sum = 0
for elem in array[min_pos+1:max_pos]:
    elem_sum += elem

print(f'Сумма элементов между минимальным {array[min_pos]} и максимальным {array[max_pos]} равна {elem_sum}')