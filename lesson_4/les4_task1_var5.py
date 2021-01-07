"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
import cProfile
import functools


def test_func(func):
    dct = {'01': '10', '0123': '3210', '5632104': '4012365',
           '13566192643362838763189695118785125752177375262366': '66326257377125752158781159698136783826334629166531'}
    for key, value in dct.items():
        assert value == func(key)
        print(f'Test {key} OK')


@functools.lru_cache()
def rec_num(num):
    """Принимает str"""
    if not num:
        return ''
    return num[-1] + rec_num(num[:-1])


# test_func(rec_num)

# 10
# "var5.rec_num('6573946186')"
# 1000 loops, best of 5: 60.5 nsec per loop
# 50
# "var5.rec_num('13566192643362838763189695118785125752177375262366')"
# 1000 loops, best of 5: 63.6 nsec per loop
# 100
# "var5.rec_num('444861847256838............
# 1000 loops, best of 5: 62.7 nsec per loop
# 200/
# "var5.rec_num('4288222141132......')"
# 1000 loops, best of 5: 61.2 nsec per loop
# предупреждение выходит всегда
# :0: UserWarning: The test results are likely unreliable. The worst time (274 nsec) was more than four times slower than the best time (61.2 nsec).
# 400
# 1000 loops, best of 5: 61.2 nsec per loop
# предупреждение выходит всегда
# :0: UserWarning: The test results are likely unreliable. The worst time (566 nsec) was more than four times slower than the best time (61.2 nsec).


# cProfile.run('rec_num("123")')
# 10
# 11/1    0.000    0.000    0.000    0.000 var5.py:16(rec_num)
# 50
# 51/1    0.000    0.000    0.000    0.000 var5.py:16(rec_num)
# 100
# 101/1    0.000    0.000    0.000    0.000 var5.py:16(rec_num)
# 500
# 501/1    0.001    0.000    0.001    0.001 var5.py:16(rec_num)
