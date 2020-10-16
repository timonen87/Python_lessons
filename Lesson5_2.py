'''
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
'''

my_file = open("file1.txt", "r")
content = my_file.read()
print(f"Файл содержит: \n {content}")

my_file = open("file1.txt", "r")
content = my_file.readline()
print(f"Количество строк в файле: {len(content)}")

my_file = open("file1.txt", "r")
content = my_file.readline()
for i, line in enumerate(content):
    print(f"Количество символов {i + 1} : строки {len(content[i])} ")

my_file = open("file1.txt", "r")
content = my_file.read()
content = content.split()
print(f"Общее количество слов в файле:{len(content)}")
my_file.close()
