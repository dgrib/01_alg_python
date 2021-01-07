line1 = int(input("Введите длинну первого отрезка: "))
line2 = int(input("Введите длинну второго отрезка: "))
line3 = int(input("Введите длинну третьего отрезка: "))
if (line1 < (line2 + line3)) and (line2 < (line1 + line3)) and (line3 < (line2 + line1)):
    if line1 == line2 == line3:
        print("Треугольник равносторонний")
    elif line2 == line3 or line2 == line1 or line3 == line1:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторнний")
else:
    print("Треугольника не существует")
