'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить
на своем месте.
Для заполнения списка элементов необходимо использовать
функцию input().
'''

el_list =int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_list:
    my_list.append((input("Введите знаение списка ")))
    i += 1
for element in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
        el += 2
print(my_list)