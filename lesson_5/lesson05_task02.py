"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
************
Работа программы: получает 2 шестнадцатеричных числа, переводит их в десятичные,
затем суммирует и умножает десятичные числа, затем переводит результат сложения и умножения в шестнадцатеричный вид.
"""
from collections import OrderedDict
from collections import deque


def get_int(hex_string):
    """Переводит шестнадцатеричное число в десятичное.
        Получает 'C4F', отдает 3151"""
    hex_list = [_ for _ in hex_string]
    int_sum = 0
    symbol_rank = 1
    for symbol in hex_list[::-1]:
        int_sum += compare_dict[str(symbol)] * symbol_rank
        symbol_rank *= 16
    return int_sum


def get_hex(num):
    """Переводит десятичное число в шестнадцатеричное.
        Получает 3151, отдает 'C4F'"""
    hex_num = deque([])

    # получаем из 3151 очередь шестнадцатеричных разрядов вида deque([12, 4, 15])
    while num > 15:
        hex_num.appendleft(num % 16)
        num //= 16
    hex_num.appendleft(num)

    # из очереди вида deque([12, 4, 15]) получаем строку вида 'C4F'
    result = ''
    for number in hex_num:
        for k, v in compare_dict.items():
            if number == v:
                result = result + k
    return result


compare_dict = OrderedDict([('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
                            ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('A', 10),
                            ('B', 11), ('C', 12), ('D', 13), ('E', 14), ('F', 15)])

marker = 1
while marker:
    first = input('Введите первое шестнадцатеричное число, англ. раскладка (например: a2, A2): ').upper()
    second = input('Введите второе шестнадцатеричное число, англ. раскладка  (например: a2, A2): ').upper()

    # проверка шестнадцатеричных чисел на валидность
    marker = 0
    for i in first:
        if i not in '0123456789ABCDEF':
            marker += 1
    for i in second:
        if i not in '0123456789ABCDEF':
            marker += 1
    if marker:
        print('Введите коректные шестнадцатеричные числа.')


hex_sum = get_hex((get_int(first) + get_int(second)))
print(f'{first} + {second} = {hex_sum}')
hex_mul = get_hex((get_int(first) * get_int(second)))
print(f'{first} * {second} = {hex_mul}')
