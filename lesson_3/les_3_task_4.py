"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randint

array = [randint(1, 10) for _ in range(20)]
print(array)

count_dict = {i: 0 for i in set(array)}
for elem in array:
    count_dict[elem] += 1

freq_elem = 0
number = 0
for key, value in count_dict.items():
    if value > number:
        number = value
        freq_elem = key

# если макс-частотное число не одно, то выводим все макс-частотные числа
for key, value in count_dict.items():
    if value == number:
        print(f'Число {key} встречается в массиве чаще всего ({number} раз(а)).')
