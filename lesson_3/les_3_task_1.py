"""
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""
count_list = [0] * 8

for digit in range(2, 10):
    for elem in range(2, 100):
        if elem % digit == 0:
            count_list[digit - 2] += 1
    print(f'Цифра {digit} кратна {count_list[digit - 2]} числам из диапазона 2...99')
# for pos, el in enumerate(count_list):
#     print(f'Цифра {pos + 2} кратна {el} числам из диапазона 2...99')

# for pos, el in enumerate(count_list, start=2):
#     print(f'Цифра {pos} кратна {el} числам из диапазона 2...99')
