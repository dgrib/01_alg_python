char1 = ord(input("Введите первую латинскую букву: "))
char2 = ord(input("Введите вторую латинскую букву: "))
num1 = char1 - ord("a") + 1
num2 = char2 - ord("a") + 1
num3 = abs(num2 - num1)
if num3 != 0:
    num3 -= 1
print(f"Номер первой буквы = {num1}")
print(f"Номер второй буквы = {num2}")
if num3 == 1:
    print(f"Между ними {num3} буква")
elif 5 <= num3 <= 10:
    print(f"Между ними {num3} букв")
elif num3 == 0:
    print(f"Между ними нет букв")
else:
    print(f"Между ними {num3} буквы")