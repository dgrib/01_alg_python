h_list = [None] * 26


def my_append(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)


a = 'apricot'
my_append(a)

b = 'banana'
my_append(b)

# хеш коллизия, где разные значения получают один и тот же хеш
c = 'apple'
my_append(c)

print(4625 == 4 * 10 ** 3 + 6 * 10 ** 2 + 2 * 10 ** 1 + 5 * 10 ** 0)


def my_index(value):
    # по сути это основание нашей системы исчисления
    letter = 26
    # тут мы будем накапливать результат
    index = 0
    # размер словаря
    size = 10000

    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i

    return index % size


print(my_index(a))
print(my_index(b))
print(my_index(c))