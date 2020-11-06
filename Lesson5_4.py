'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские
числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три' , 'Four' : 'Четыре'}
new_file = []
with open('file3.txt', 'r') as f_obj:
    #content = f_obj.read().split('\n')
    for i in f_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with open('file3new.txt', 'w') as f_obj_2:
    f_obj_2.writelines(new_file)