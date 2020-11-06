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
        res = (20 * (time * rate)) + bonus   #С учетом 20 рабочих дней в месяце.
        print(f"Заработная плата в месяц  {res}")
        print(f"Премия  {bonus}")
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
    res = (20 * (time * rate)) + bonus
    print(f"Заработная плата в месяц  {res}")
    print(f"Премия  {bonus}")
except ValueError:
    print("Значение не введено")
