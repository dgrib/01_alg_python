number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
if number2 < number1 < number3 or number3 < number1 < number2:
    print("Среднее число номер 1")
elif number1 < number2 < number3 or number3 < number2 < number1:
    print("Среднее число номер 2")
elif number2 < number3 < number1 or number1 < number3 < number2:
    print("Среднее число номер 3")
elif number1 == number2 == number3:
    print("Все числа равны, невозможно определить среднее")
elif number1 == number2 or number1 == number3 or number2 == number3:
    print("Некоторые числа равны, нельзя определить среднее")
