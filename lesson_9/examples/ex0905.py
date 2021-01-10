import hashlib


def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустые'

    # берем строку из переменной а, переводим в utf-8
    # получается байт строка,
    # эти байты передаем в алгоритм хеширования sha1
    # полученный результат представляем в виде 16 строки
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f'hash 1 = {ha}\nhash 2 = {hb}')

    return ha == hb


s_1 = input('Введите строку 1: ')
s_2 = input('Введите строку 2: ')

print('Строки одинаковые' if is_eq_str(s_1, s_2, True) else 'Строки разные')
