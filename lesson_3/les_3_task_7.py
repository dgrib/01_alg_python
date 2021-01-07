"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
# from random import randint
#
# array = [randint(1, 30) for _ in range(20)]
# print(array)
#
# first_min = 30
# first_min_pos = 0
#
# for pos, elem in enumerate(array):
#     if elem < first_min:
#         first_min, first_min_pos = elem, pos
#
# new_array = array[:first_min_pos] + array[first_min_pos+1:]
# second_min = 30
#
# for elem in new_array:
#     if elem < second_min:
#         second_min = elem
#
# print(f'Первый минимальный элемент массива равен {first_min}.')
# print(f'Второй минимальный элемент массива равен {second_min}.')


from random import randint

array = [randint(-50, 50) for _ in range(20)]
print(array)

if array[0] < array[1]:
    first_min_index = 0
    second_min_index = 1
else:
    first_min_index = 1
    second_min_index = 0

for i in range(2, len(array)):
    if array[i] < array[first_min_index]:
        second_min_index = first_min_index
        first_min_index = i
    elif array[first_min_index] < array[i] < array[second_min_index]:
        second_min_index = i

print(f'Первый минимальный элемент массива равен {array[first_min_index]}.')
print(f'Второй минимальный элемент массива равен {array[second_min_index]}.')
