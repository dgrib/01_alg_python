"""5. Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
"""

letter_num = int(input('Введите номер буквы (1-26): '))
print(f'{letter_num}-я буква в англ. алфавите: {chr(letter_num + 96)}')
