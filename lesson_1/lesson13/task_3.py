let1 = input('Введите букву 1: ')
let2 = input('Введите букву 2: ')
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(characters.index(let1) + 1, characters.index(let2) + 1, characters.index(let2) - characters.index(let1) - 1)