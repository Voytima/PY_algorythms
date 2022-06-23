# 1) Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections

companies = {}
n = int(input('Number of companies: '))
quarter = 4
inc = 0
profit_comp = collections.deque()
unprofit_comp = collections.deque()

for i in range(n):
    name = input('Enter company name: ')
    inc_per_fac = 0
    if name in companies:
        print('Company already exists')
        break
    else:
        for j in range(quarter):
            inc_per_fac += float(input(f"{str(j + 1)} quarter income is: "))
    companies[name] = inc_per_fac
    inc += inc_per_fac

avg_income = inc / n
print('*'*50)
print(f'Total average income per year: |{avg_income:.1f}| rub.')

for i, item in companies.items():
    if item > avg_income:
        profit_comp.append(i)
    else:
        unprofit_comp.append(i)

print(f'Average income per company:\n{companies}')
print('*'*50)
print(f'Companies with profit has(have) {len(profit_comp)} company(-ies):')
for name in profit_comp:
    print(name)
print('-' * 50)
print(f'Companies with no profit has(have) {len(unprofit_comp)} company(-ies):')
for name in unprofit_comp:
    print(name)

# **************** Можно еще реализовать через "Именованный кортеж" ***************************

from collections import namedtuple


company = namedtuple('company', ['name', 'quarters', 'income'])
all_companies = set()   # Для хранения всех компаний (защита от дубликатов в том числе)
quarter = 4

n = int(input('How many companies: '))  # Количество предприятий
total_income = 0    # Общая прибыль компаний

"""Внешний цикл для ввода имени предприятия, и сохранения прибыли; внутренний цикл для рассчета прибыли по кварталам"""
for i in range(1, n + 1):
    income = 0      # Прибыль для конкретного предприятия
    quarters = []   # Прибыль предприятия за каждый квартал
    name = input(f'Enter company name {i}: ')   # имя предприятия

    for j in range(quarter):
        quarters.append(int(input(f'Income for {j + 1} quarter is: ')))
        income += quarters[j]   # Суммируем профит за год

    comp = company(name=name, quarters=tuple(quarters), income=income)
    all_companies.add(comp)
    total_income += income

avg_income = total_income / n   # Средняя прибыль за год

print(f'Average income: {avg_income} rub')

"""Выводим предприятия с профитом выше среднего и ниже среднего в этом году"""
print(f'\nCompanies with income above average:')
for comp in all_companies:
    if comp.income > avg_income:
        print(f'Company {comp.name} ---> {comp.income} rub')

print(f'\nCompanies with income below average:')
for comp in all_companies:
    if comp.income < avg_income:
        print(f'Company {comp.name} ---> {comp.income} rub')