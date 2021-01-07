# -*- coding: utf-8 -*-
"""
Будем анализировать задачу 2.3
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
import sys


def print_size(obj, indent=0):
    consumption = sys.getsizeof(obj)
    print('\t'*indent, f'{obj.__class__}, size: {sys.getsizeof(obj)}', end='', sep='')
    if isinstance(obj, list):
        print()
        for a in obj:
            print_size(a, indent + 1)
    else:
        print('\t'*indent, f'value: {obj}')
    return consumption


def print_locals(d, ignore='num'):
    total = 0
    for k, v in d.items():
        if k == ignore:
            continue
        print('\t', k, end='', sep='')
        total += print_size(v, 2)
    print(f'\ttotal: {total}')


def revers_num_classic(num):
    digits = 0
    n = num
    while num:
        num //= 10
        digits += 1
    mul = 10 ** (digits - 1)
    rev_num = 0
    while mul:
        n, digit = divmod(n, 10)
        rev_num += digit * mul
        mul //= 10
    print_locals(locals())
    return rev_num


def reverse_num_reversed(num):
    a = str(num)
    b = reversed(a)
    c = ''.join(b)
    print_locals(locals())
    return int(c)


def reverse_num_list(num):
    a = []
    while num:
        num, digit = divmod(num, 10)
        a.append(str(digit))
    b = ''.join(a)
    print_locals(locals())
    return int(b)


def reverse_num_slice(num):
    a = str(num)
    b = list(a)
    c = b[::-1]
    d = ''.join(c)
    print_locals(locals())
    return int(d)


if __name__ == '__main__':
    number = 4567
    print(f'Платформа {sys.platform}, версия {sys.version}')
    print('revers_num_classic')
    answer = revers_num_classic(number)
    print('reverse_num_reversed')
    answer = reverse_num_reversed(number)
    print('reverse_num_list')
    answer = reverse_num_list(number)
    print('reverse_num_slice')
    answer = reverse_num_slice(number)

"""
Платформа win32, версия 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)]
revers_num_classic
	digits		<class 'int'>, size: 14		 value: 4
	n		<class 'int'>, size: 12		 value: 0
	mul		<class 'int'>, size: 12		 value: 0
	rev_num		<class 'int'>, size: 14		 value: 7654
	digit		<class 'int'>, size: 14		 value: 4
	total: 66
reverse_num_reversed
	a		<class 'str'>, size: 29		 value: 4567
	b		<class 'reversed'>, size: 32		 value: <reversed object at 0x01933170>
	c		<class 'str'>, size: 29		 value: 7654
	total: 90
reverse_num_list
	a		<class 'list'>, size: 52
			<class 'str'>, size: 26			 value: 7
			<class 'str'>, size: 26			 value: 6
			<class 'str'>, size: 26			 value: 5
			<class 'str'>, size: 26			 value: 4
	digit		<class 'int'>, size: 14		 value: 4
	b		<class 'str'>, size: 29		 value: 7654
	total: 95
reverse_num_slice
	a		<class 'str'>, size: 29		 value: 4567
	b		<class 'list'>, size: 64
			<class 'str'>, size: 26			 value: 4
			<class 'str'>, size: 26			 value: 5
			<class 'str'>, size: 26			 value: 6
			<class 'str'>, size: 26			 value: 7
	c		<class 'list'>, size: 52
			<class 'str'>, size: 26			 value: 7
			<class 'str'>, size: 26			 value: 6
			<class 'str'>, size: 26			 value: 5
			<class 'str'>, size: 26			 value: 4
	d		<class 'str'>, size: 29		 value: 7654
	total: 174
"""
"""
Как и ожидалось, если не использовать списки и строки, то и памяти надо меньше всего.

Так для revers_num_classic понадобилось всего 66 байт

Далее, reversed - это особый объект-итератор, он много места не занимает, в отличае от списков строк. Чем больше будет
список, тем больше и выигрыш.

Каждая буква - это строка, поэтому список строк в сумме(с содержимым) занимает относительно много места, в случае с
reverse_num_list - 95 байт, хоть и не на много, но больше, чем в версии с использованием reversed

Ну и reverse_num_slice съедает больше всего, так как при использовании slice список дублируется

Я бы выбрал версию reverse_num_reversed как лучшую, так как не так много потребляет по памяти, а код довольно
минималистичный получается.
Но, если надо прямо сэкономить память, то можно подобрать алгоритм без использования строк и коллекций
"""
