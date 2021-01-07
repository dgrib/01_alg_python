"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки)
вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
ЗАДАНИЕ: Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
Изменяю условие: программа должна вывести не количество цифр, а сами эти цифры.
Чтобы было больше разных вариантов подсчета памяти под переменные.
"""
import sys
import ctypes
import struct
from collections import deque


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


num = int(input("Введите число: "))
num_copy = num
digit = 0
even = deque([])
uneven = deque([])
if num == 0:
    even.append('0')  # ноль это четное число

while num:
    digit = num % 10
    if digit % 2 == 0:
        even.appendleft(digit)
    else:
        uneven.appendleft(digit)
    num //= 10

print(f'Четные цифры в числе {num_copy}: {even}')
print(f'Нечетные цифры в числе {num_copy}: {uneven}')

print(sys.version, sys.platform)
show_size(num)
show_size(num_copy)
show_size(digit)
show_size(even)
show_size(uneven)

"""
Введите число: 12
Четные цифры в числе 12: deque([2])
Нечетные цифры в числе 12: deque([1])
3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] win32
 type= <class 'int'>, size= 24, object= 0
 type= <class 'int'>, size= 28, object= 12
 type= <class 'int'>, size= 28, object= 1
 type= <class 'collections.deque'>, size= 624, object= deque([2])
	 type= <class 'int'>, size= 28, object= 2
 type= <class 'collections.deque'>, size= 624, object= deque([1])
	 type= <class 'int'>, size= 28, object= 1
"""

"""
Введите число: 1234567890
Четные цифры в числе 1234567890: deque([2, 4, 6, 8, 0])
Нечетные цифры в числе 1234567890: deque([1, 3, 5, 7, 9])
3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] win32
 type= <class 'int'>, size= 24, object= 0
 type= <class 'int'>, size= 32, object= 1234567890
 type= <class 'int'>, size= 28, object= 1
 type= <class 'collections.deque'>, size= 1152, object= deque([2, 4, 6, 8, 0])
	 type= <class 'int'>, size= 28, object= 2
	 type= <class 'int'>, size= 28, object= 4
	 type= <class 'int'>, size= 28, object= 6
	 type= <class 'int'>, size= 28, object= 8
	 type= <class 'int'>, size= 24, object= 0
 type= <class 'collections.deque'>, size= 1152, object= deque([1, 3, 5, 7, 9])
	 type= <class 'int'>, size= 28, object= 1
	 type= <class 'int'>, size= 28, object= 3
	 type= <class 'int'>, size= 28, object= 5
	 type= <class 'int'>, size= 28, object= 7
	 type= <class 'int'>, size= 28, object= 9
"""

"""
Введите число: 13566192643362838763189695118785125752177375262366
Четные цифры в числе 13566192643362838763189695118785125752177375262366: deque([6, 6, 2, 6, 4, 6, 2, 8, 8, 6, 8, 6, 8, 8, 2, 2, 2, 6, 2, 6, 6])
Нечетные цифры в числе 13566192643362838763189695118785125752177375262366: deque([1, 3, 5, 1, 9, 3, 3, 3, 7, 3, 1, 9, 9, 5, 1, 1, 7, 5, 1, 5, 7, 5, 1, 7, 7, 3, 7, 5, 3])
3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] win32
 type= <class 'int'>, size= 24, object= 0
 type= <class 'int'>, size= 48, object= 13566192643362838763189695118785125752177375262366
 type= <class 'int'>, size= 28, object= 1
 type= <class 'collections.deque'>, size= 1152, object= deque([6, 6, 2, 6, 4, 6, 2, 8, 8, 6, 8, 6, 8, 8, 2, 2, 2, 6, 2, 6, 6])
	 type= <class 'int'>, size= 28, object= 6
	 type= <class 'int'>, size= 28, object= 6
	 type= <class 'int'>, size= 28, object= 2
	 type= <class 'int'>, size= 28, object= 6
	 type= <class 'int'>, size= 28, object= 4
	 type= <class 'int'>, size= 28, object= 6
	 type= <class 'int'>, size= 28, object= 2
	 type= <class 'int'>, size= 28, object= 8
	 type= <class 'int'>, size= 28, object= 8
	 type= <class 'int'>, size= 28, object= 6
	 type= <class 'int'>, size= 28, object= 8
	 type= <class 'int'>, size= 28, object= 6
	 type= <class 'int'>, size= 28, object= 8
	 type= <class 'int'>, size= 28, object= 8
	 type= <class 'int'>, size= 28, object= 2
	 type= <class 'int'>, size= 28, object= 2
	 type= <class 'int'>, size= 28, object= 2
	 type= <class 'int'>, size= 28, object= 6
	 type= <class 'int'>, size= 28, object= 2
	 type= <class 'int'>, size= 28, object= 6
	 type= <class 'int'>, size= 28, object= 6
 type= <class 'collections.deque'>, size= 1152, object= deque([1, 3, 5, 1, 9, 3, 3, 3, 7, 3, 1, 9, 9, 5, 1, 1, 7, 5, 1, 5, 7, 5, 1, 7, 7, 3, 7, 5, 3])
	 type= <class 'int'>, size= 28, object= 1
	 type= <class 'int'>, size= 28, object= 3
	 type= <class 'int'>, size= 28, object= 5
	 type= <class 'int'>, size= 28, object= 1
	 type= <class 'int'>, size= 28, object= 9
	 type= <class 'int'>, size= 28, object= 3
	 type= <class 'int'>, size= 28, object= 3
	 type= <class 'int'>, size= 28, object= 3
	 type= <class 'int'>, size= 28, object= 7
	 type= <class 'int'>, size= 28, object= 3
	 type= <class 'int'>, size= 28, object= 1
	 type= <class 'int'>, size= 28, object= 9
	 type= <class 'int'>, size= 28, object= 9
	 type= <class 'int'>, size= 28, object= 5
	 type= <class 'int'>, size= 28, object= 1
	 type= <class 'int'>, size= 28, object= 1
	 type= <class 'int'>, size= 28, object= 7
	 type= <class 'int'>, size= 28, object= 5
	 type= <class 'int'>, size= 28, object= 1
	 type= <class 'int'>, size= 28, object= 5
	 type= <class 'int'>, size= 28, object= 7
	 type= <class 'int'>, size= 28, object= 5
	 type= <class 'int'>, size= 28, object= 1
	 type= <class 'int'>, size= 28, object= 7
	 type= <class 'int'>, size= 28, object= 7
	 type= <class 'int'>, size= 28, object= 3
	 type= <class 'int'>, size= 28, object= 7
	 type= <class 'int'>, size= 28, object= 5
	 type= <class 'int'>, size= 28, object= 3
	 """