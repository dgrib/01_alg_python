"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple


def digit_input(message):
    """Проверяет, что ввод пользователя является числом."""
    while True:
        user_num = input(message)
        if user_num.isdigit():
            break
    return int(user_num)


firms_num = digit_input('Введите количество предприятий: ')
firm_template = ['name', 'kv_1', 'kv_2', 'kv_3', 'kv_4', 'year_income']
New_Firm = namedtuple('New_Firm', firm_template)
firms_list = []
all_firm_income = 0

for firm_num in range(firms_num):

    name = input(f'Введите наименование предприятия {firm_num + 1}: ')

    # хранение воодных данных для 4 кварталов
    temp_data = []
    for season in firm_template[1:-1]:
        temp_data.append(digit_input(f'Введите прибыль для квартала {season}: '))
    firm_year_income = sum(temp_data)
    # добавляем предприятие в список предприятий
    firms_list.append(New_Firm(name, *temp_data, firm_year_income))
    # добавляем суммарный доход предприятия к общему для подсчета среднего
    all_firm_income += firm_year_income

average_income = all_firm_income / firms_num

# вывод всех фирм и их годового дохода
print()
print('*' * 50)
for firm in firms_list:
    print(f'Предприятие {firm.name.upper()} имеет годовую прибыль {firm.year_income}')

# вывод годовых доходов фирм по отношению к среднему доходу
print('*' * 50)
print(f'Организции с годовым доходом выше среднего ({average_income}):')
for i in firms_list:
    if i.year_income > average_income:
        print(f'Предприятие {i.name.upper()} имеет годовую прибыль {i.year_income}')

print(f'Организции с годовым доходом ниже среднего ({average_income}):')
for i in firms_list:
    if i.year_income < average_income:
        print(f'Предприятие {i.name.upper()} имеет годовую прибыль {i.year_income}')
