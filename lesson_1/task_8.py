"""8. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).
"""

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
string = f'Среди чисел {a, b, c} среднее: '

if a > b and a > c:
    if b > c:
        print(f'{string}{b}')
    else:
        print(f'{string}{c}')
elif b > c and b > a:
    if a > c:
        print(f'{string}{a}')
    else:
        print(f'{string}{c}')
else:
    if a > b:
        print(f'{string}{a}')
    else:
        print(f'{string}{b}')
