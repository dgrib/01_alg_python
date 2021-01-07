"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
from math import log
import cProfile


def test_func(func):
    dct = {1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13, 20: 71, 500: 3571}
    for key, value in dct.items():
        assert value == func(key)
        print(f'Test {key} OK')


def get_upper_border(i):
    """Возвращает верхнюю границу отрезка на котором лежат i-e количество простых чисел.
    Функция основана на теореме о распределении простых чисел, она утверждает,
    что количество простых чисел на отрезке [1;n] растёт с увеличением n как n / ln(n).
    """

    number = 0
    upper_border = 2

    while number <= i:
        number = upper_border / log(upper_border)
        upper_border += 1
    # 1 добавляем, чтобы количество чисел наверняка было внутри [1;n]
    return upper_border + 1


def i_simple_erat(n):
    upper_border = get_upper_border(n)
    sieve = [i for i in range(upper_border)]
    sieve[1] = 0

    for num in range(2, upper_border):
        if sieve[num] != 0:
            j = num * 2
            while j < upper_border:
                sieve[j] = 0
                j += num

    simple_list = [i for i in sieve if i != 0]
    return simple_list[n - 1]


# test_func(i_simple_erat)
# i_simple = int(input('Введите какое по счету простое число вывести: '))
# print(i_simple_erat(i_simple))

# "var1.i_simple_erat(1)"
# 1000 loops, best of 5: 1.21 usec per loop
# "var1.i_simple_erat(5)"
# 1000 loops, best of 5: 4.3 usec per loop
# "var1.i_simple_erat(10)"
# 1000 loops, best of 5: 11.1 usec per loop
# "var1.i_simple_erat(20)"
# 1000 loops, best of 5: 28.1 usec per loop
# "var1.i_simple_erat(50)"
# 1000 loops, best of 5: 90.6 usec per loop
# "var1.i_simple_erat(100)"
# 1000 loops, best of 5: 223 usec per loop
# "var1.i_simple_erat(200)"
# 1000 loops, best of 5: 512 usec per loop
# "var1.i_simple_erat(500)"
# 1000 loops, best of 5: 1.5 msec per loop
# "var1.i_simple_erat(1000)"
# 1000 loops, best of 5: 3.37 msec per loop

# cProfile.run('i_simple_erat(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.073    0.073 <string>:1(<module>)
#         1    0.022    0.022    0.037    0.037 var1.py:22(get_upper_border)
#         1    0.028    0.028    0.072    0.072 var1.py:38(i_simple_erat)
#         1    0.004    0.004    0.004    0.004 var1.py:40(<listcomp>)
#         1    0.003    0.003    0.003    0.003 var1.py:50(<listcomp>)
#         1    0.000    0.000    0.073    0.073 {built-in method builtins.exec}
#    116671    0.015    0.000    0.015    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
