"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
import cProfile


def test_func(func):
    dct = {'01': '10', '0123': '3210', '5632104': '4012365'}
    for key, value in dct.items():
        assert value == func(key)
        print(f'Test {key} OK')


def rec_num(num):
    """Принимает str"""
    line = ''
    for symbol in num[::-1]:
        line += symbol
    return line


# test_func(rec_num)
# 10
# "var2.rec_num('6573946186')"
# 1000 loops, best of 5: 677 nsec per loop
# 50
# "var2.rec_num('13566192643362838763189695118785125752177375262366')"
# 1000 loops, best of 5: 2.69 usec per loop
# 100
# "var2.rec_num('4448618472568382615...........
# 1000 loops, best of 5: 5.05 usec per loop
# 500
# "var2.rec_num('561223814622236.......
# 1000 loops, best of 5: 29 usec per loop
# 1000
# "var2.rec_num('25469313641613668.....
# 1000 loops, best of 5: 110 usec per loop
# 10000
# "var2.rec_num('8941151427......
# 1000 loops, best of 5: 1.39 msec per loop

# cProfile.run('rec_num("6573946186")')
# 10
# 1    0.000    0.000    0.000    0.000 var2.py:16(rec_num)
# 50
# 1    0.000    0.000    0.000    0.000 var2.py:16(rec_num)
# 100
# 1    0.000    0.000    0.000    0.000 var2.py:16(rec_num)
# 500
# 1    0.000    0.000    0.000    0.000 var2.py:16(rec_num)
# 1000
# 1    0.000    0.000    0.000    0.000 var2.py:16(rec_num)
# 10000
# 1    0.001    0.001    0.001    0.001 var2.py:16(rec_num)

