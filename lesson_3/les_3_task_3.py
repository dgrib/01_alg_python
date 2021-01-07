"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
# from random import randint
#
# array = [randint(1, 100) for _ in range(20)]
# print(array)
#
# min_elem = 100
# max_elem = 0
# pos_min = 0
# pos_max = 0
#
# for pos, elem in enumerate(array):
#     if elem > max_elem:
#         max_elem = elem
#         pos_max = pos
#     if elem < min_elem:
#         min_elem = elem
#         pos_min = pos
#
# print(f'Максимальный элемент в массиве {max_elem}, его позиция {pos_max + 1}')
# print(f'Минимальный элемент в массиве {min_elem}, его позиция {pos_min + 1}')
#
# array[pos_max], array[pos_min] = min_elem, max_elem
# print(f'\nМассив, в котором max и min элементы поменяны местами:\n{array}')


from random import randint

array = [randint(1, 100) for _ in range(20)]
print(array)

pos_min = 0
pos_max = 0

for pos in range(len(array)):
    if array[pos] > array[pos_max]:
        pos_max = pos
    if array[pos] < array[pos_min]:
        pos_min = pos

print(f'Максимальный элемент в массиве {array[pos_max]}, его позиция {pos_max + 1}')
print(f'Минимальный элемент в массиве {array[pos_min]}, его позиция {pos_min + 1}')

array[pos_max], array[pos_min] = array[pos_min], array[pos_max]
print(f'\nМассив, в котором max и min элементы поменяны местами:\n{array}')
