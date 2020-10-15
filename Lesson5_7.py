'''
    Создать вручную и заполнить несколькими строками текстовый файл,
    в котором каждая строка должна содержать данные о фирме:
    название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1   ООО   10000   5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой
    компании, а также среднюю прибыль. Если фирма получила убытки,
    в расчет средней прибыли ее не включать.
    Далее реализовать список. Он должен содержать словарь 
    с фирмами и их прибылями, а также словарь со средней прибылью. 
    Если фирма получила убытки, также добавить ее в словарь 
    (со значением убытков).
    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, 
    {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий 
    файл.
    Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, 
    {"average_profit": 2000}]
    Подсказка: использовать менеджер контекста.
'''
import json

profit = {}
profit_av = {}
prof = 0
prof_average = 0
i = 0
with open('file7.txt', 'r') as file:
    for line in file:
        name, company, revenue, expenses = line.split()
        profit[name] = int(revenue) - int(expenses)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_average = prof / i
        print(f'Прибыль средняя - {prof_average:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    profit_av = {'средняя прибыль': round(prof_average)}
    profit.update(profit_av)
    print(f'Прибыль каждой компании - {profit}')

with open('file7.json', 'w') as file_json:
    json.dump(profit, file_json)

    json_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {json_str}')