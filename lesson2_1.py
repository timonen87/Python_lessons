'''
Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт определения типа данных каждого элемента.
 Использовать функцию type() для проверки типа. 
 Элементы списка можно не запрашивать у пользователя, а указать явно, в программе. 
 Попробуйте использовать не только базовые типы, но и вложенные словари, кортежи, списки.
 (Можно ограничиться вложенностью 1 уровня и не обходить содержимое этих вложенных коллекций.)
'''

list_el = [23, 'cycle', None, -50, False, 4.5]
def List_type (el):
    for el in range(len(list_el)):
        print(type(list_el[el]))
    return
List_type(list_el)
