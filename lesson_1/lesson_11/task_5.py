# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

char1 = int(input("Введите номер буквы от 1 до 26: "))
if char1 < 1 or char1 > 26:
    print("Неверный ввод!")
else:
    print(chr(char1+96))
