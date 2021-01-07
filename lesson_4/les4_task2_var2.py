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
import cProfile


def test_func(func):
    dct = {1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13, 20: 71, 500: 3571}
    for key, value in dct.items():
        assert value == func(key)
        print(f'Test {key} OK')


def i_simple(n):
    probe = 1
    simple_list = []

    while len(simple_list) < n:
        probe += 1
        for i in range(2, probe):
            if probe % i == 0:
                break
        else:
            simple_list.append(probe)

    return simple_list[-1]


# test_func(i_simple)
# n = int(input('Введите какое по счету простое число вывести: '))
# print(i_simple(n))


# "var2.i_simple(1)"
# 1000 loops, best of 5: 342 nsec per loop
# "import var2" "var2.i_simple(5)"
# 1000 loops, best of 5: 3.03 usec per loop
# "var2.i_simple(10)"
# 1000 loops, best of 5: 10.2 usec per loop
# "var2.i_simple(20)"
# 1000 loops, best of 5: 35.9 usec per loop
# "var2.i_simple(50)"
# 1000 loops, best of 5: 215 usec per loop
# "var2.i_simple(100)"
# 1000 loops, best of 5: 960 usec per loop
# "var2.i_simple(200)"
# 1000 loops, best of 5: 4.69 msec per loop
# "var2.i_simple(500)"
# 1000 loops, best of 5: 34 msec per loop
# "var2.i_simple(1000)"
# 1000 loops, best of 5: 156 msec per loop


# cProfile.run('i_simple(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   21.074   21.074 <string>:1(<module>)
#         1   21.063   21.063   21.073   21.073 var2.py:21(i_simple)
#         1    0.000    0.000   21.074   21.074 {built-in method builtins.exec}
#    104729    0.009    0.000    0.009    0.000 {built-in method builtins.len}
#     10000    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
