'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа,
начиная с указанного,
б) бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle()
модуля itertools.
'''

from itertools import count

for el in count(int(input("Введите стартовое число "))):
    print(el) # беконечный цикл!

from itertools import cycle

my_list = [False, 'cycle', None, 567]
for el in cycle(my_list):
    print(el) # беконечный цикл!