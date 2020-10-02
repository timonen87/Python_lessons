my_str = input("Введите строку из нескольких слов ")
my_word =[]
number = 1
for el in range(my_str.count(' ') + 1):  #считаем количество введенных слов, + 1 т.к. number = 1
    my_word = my_str.split()             #Разбиваем строку по разделителю с помошью split()
    if len(str(my_word)) <= 10:          #Если длина слова меньше или равное 10 
        print(f"{number} {my_word[el]}") # Выводим номер и слово
    else:
        print((f" {number} {my_word [el] [0:10]}"))  # Длина слова больше 10, выводим только первые 10 букв.
        number +=1      