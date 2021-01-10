"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter, OrderedDict


class MyNode:

    def __init__(self, leaf=False, left=None, right=None):
        self.left = left
        self.right = right
        self.leaf = leaf

    def search(self, symbol, code=''):

        if self.leaf:
            encoding_dict[symbol] = code
        elif symbol in self.left:
            node_heap[self.left].search(symbol, code + '0')
        elif symbol in self.right:
            node_heap[self.right].search(symbol, code + '1')


s = 'begin began begun'
print(f'Исходная строка: {s}')
# получаем словарь частотности символов
symbols = OrderedDict(reversed(Counter(s).most_common()))
print(f'Частота букв в строке:')
for k, v in symbols.items():
    print(f"'{k}' = {v}  ", end='')
print()
print()

# храним кортежи для последующего формирования node_heap
node_list = []
# храним экземпляры классов MyNode
node_heap = {}
for k, v in symbols.items():
    node_list.append((k, v))
    node_heap[k] = MyNode(leaf=True)

while len(node_list) > 0:
    if len(node_list) == 1:
        node_name = pre_last[0] + last[0]
        node_heap['root'] = MyNode()
        node_heap['root'].left = pre_last[0]
        node_heap['root'].right = last[0]
        break

    # берем 0 и 1 элементы списка и компануем в узел
    node_name = node_list[0][0] + node_list[1][0]
    node_heap[node_name] = MyNode()
    node_heap[node_name].left = node_list[0][0]
    node_heap[node_name].right = node_list[1][0]

    freq_sum = node_list[0][1] + node_list[1][1]

    # удаляем 2 первых элемента списка, если в списке остался 1 элемент, то используются
    # для формирования экземпляра root класса MyNode
    pre_last = node_list.pop(0)
    last = node_list.pop(0)

    # добавляем в список узел согласно сумме частотности
    for i, item in enumerate(node_list):
        if item[1] > freq_sum:
            node_list.insert(i, (node_name, freq_sum))
            break
    else:
        node_list.append((node_name, freq_sum))

# print(node_heap)
encoding_dict = {}

print('Таблица кодировки:')
for letter in symbols:
    node_heap["root"].search(letter[0])
for k, v in encoding_dict.items():
    print(f"'{k}' = {v}  ", end='')
print()
print()

print(f'Закодированная строка:', end=' ')
for i in s:
    print(f'{encoding_dict[i]}', end=' ')
print()
