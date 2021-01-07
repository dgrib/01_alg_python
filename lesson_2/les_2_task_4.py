"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""
# # решение без рекурсии
# num = int(input("Введите кол-во элементов ряда 1, -0.5, 0.25, -0.125 ... : "))
# start = 1
# all_sum = 0
# for i in range(num):
#     all_sum += start
#     start = start / -2
#
# print(all_sum)


# решение с рекурсией
def rec_sum(start, num):
    if num == 0:
        return 0
    return start + rec_sum(start / -2, num - 1)


num = int(input("Введите кол-во элементов ряда 1, -0.5, 0.25, -0.125 ... : "))
print(rec_sum(1, num))
