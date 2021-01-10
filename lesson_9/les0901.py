"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша
(hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.)
"""
import hashlib


def find_subs(s: str):
    if len(s) < 2:
        return 'Строка слишком мала'

    sub_num = 0
    sub_hashes_set = set()

    # перебираем возможные длины подстрок
    for sub_length in range(1, len(s)):
        # для каждой длины подстроки ищем подстроку в строке
        for i in range(len(s) - sub_length + 1):
            # заносим хеш подстроки во множество, если такой хеш уже есть, то множество не меняется
            sub_hashes_set.add(hashlib.sha1(s[i:i + sub_length].encode('utf-8')).hexdigest())

    return len(sub_hashes_set)


s = input('Введите строку (из строчных латинских букв): ')
print(f'В строке "{s}" количество различных подстрок: {find_subs(s)}')
