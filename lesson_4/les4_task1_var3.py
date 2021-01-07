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
    return ''.join(reversed(num))


# test_func(rec_num)
# 10
# "var3.rec_num('6573946186')"
# 1000 loops, best of 5: 463 nsec per loop
# 50
# "var3.rec_num('13566192643362838763189695118785125752177375262366')"
# 1000 loops, best of 5: 1.17 usec per loop
# 100
# "var3.rec_num('4448618472568382615......
# 1000 loops, best of 5: 1.95 usec per loop
# 500
# "var3.rec_num('56122381462......
# 1000 loops, best of 5: 7.82 usec per loop
# 1000
# "var3.rec_num('25469313641613..........
# 1000 loops, best of 5: 15.2 usec per loop
# 10000
# "var3.rec_num('89411514274945........
# 1000 loops, best of 5: 119 usec per loop


cProfile.run('rec_num("")')
# 10
# 1    0.000    0.000    0.000    0.000 var3.py:15(rec_num)
# 50
# 1    0.000    0.000    0.000    0.000 var3.py:15(rec_num)
# 100

# 500

# 1000

# 10000
# 1    0.000    0.000    0.000    0.000 var3.py:15(rec_num)
