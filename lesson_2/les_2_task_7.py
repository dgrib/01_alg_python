"""
7. Написать программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""
num = int(input("Введите число: "))
left_sum = 0
right_sum = num * (num + 1) / 2

for i in range(1, num + 1):
    left_sum += i
if left_sum == right_sum:
    print(f"Выражение 1+2+...+n = n(n+1)/2 для n = {num} выполняется!")
    print(f'{left_sum} = {int(right_sum)}')
else:
    print(f"Выражение 1+2+...+n = n(n+1)/2 для n = {num} НЕ выполняется!")
    print(f'{left_sum} != {int(right_sum)}')