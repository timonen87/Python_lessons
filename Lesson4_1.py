'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

'''

def zp():
    try:
        time = int(input("Введите выработку в час "))
        rate = int(input("Введите ставку в у.е. "))
        bonus = int(input("Введите размер премии в у.е. "))
        res = time * rate + bonus
        print(f"Заработная плата - {res}")
    except ValueError:
        return print("Значение не введено")
zp()


# Скрипт с параметрами 

from sys import argv

name, time, rate, bonus = argv
try:
    time = int(time)
    rate = int(rate)
    bonus = int(bonus)
    res = time * rate + bonus
    print(f'Заработная плата  {res}')
except ValueError:
    print('Значение не введено')
