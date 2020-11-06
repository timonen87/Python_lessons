'''
Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_file = open('test.txt', 'w')
line_text = input('Введите текст \n')
while line_text:
    my_file.writelines(line_text)
    line_text = input('Введите текст \n')
    if not line_text:
        break

my_file.close()
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
