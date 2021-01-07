"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
import cProfile
import functools


def test_func(func):
    dct = {'01': '10', '0123': '3210', '5632104': '4012365'}
    for key, value in dct.items():
        assert value == func(key)
        print(f'Test {key} OK')


def rec_num(num):
    """Принимает str"""
    if not num:
        return ''
    return num[-1] + rec_num(num[:-1])


# test_func(rec_num)

# 10
# "import var1" "var1.rec_num('6573946186')"
# 1000 loops, best of 5: 1.83 usec per loop
# 50
# "var1.rec_num('13566192643362838763189695118785125752177375262366')"
# 1000 loops, best of 5: 8.55 usec per loop
# 100
# "var1.rec_num('444861847256838............
# 1000 loops, best of 5: 17.2 usec per loop
# 200
# "var1.rec_num('4288222141132......')"
# 1000 loops, best of 5: 36.3 usec per loop
# 500
# "var1.rec_num('5612238146222......')"
# 1000 loops, best of 5: 119 usec per loop


# cProfile.run('rec_num("6573946186")')
# 10
# 11/1    0.000    0.000    0.000    0.000 var1.py:16(rec_num)
# 50
# 51/1    0.000    0.000    0.000    0.000 var1.py:16(rec_num)
# 100
# 101/1    0.000    0.000    0.000    0.000 var1.py:16(rec_num)
# 200
# 201/1    0.000    0.000    0.000    0.000 var1.py:16(rec_num)
# 500
# 501/1    0.001    0.000    0.001    0.001 var1.py:16(rec_num)
