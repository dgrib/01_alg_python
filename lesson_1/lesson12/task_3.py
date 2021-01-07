import random

down = int(input("Введите нижнюю границу: "))
up = int(input("Введите верхнюю границу: "))
number = random.randint(down, up)
print(number)
down = int(input("Введите нижнюю границу: "))
up = int(input("Введите верхнюю границу: "))
number2 = random.uniform(down, up)
print(number2)
down = ord(input("Введите нижнюю границу(любую строчную букву): "))
up = ord(input("Введите верхнюю границу(любую строчную букву): "))
char = random.randint(down, up)
print(chr(char))
