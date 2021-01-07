"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
num = int(input("Введите число: "))
num_copy = num
even = ''
uneven = ''
if num == 0:
    even = '0'  # ноль это четное число

while num:
    digit = num % 10
    if digit % 2 == 0:
        even += str(digit)
    else:
        uneven += str(digit)
    num //= 10

print(f'Четные цифры в числе {num_copy}: {", ".join(reversed(even))}')
print(f'Нечетные цифры в числе {num_copy}: {", ".join(reversed(uneven))}')
