'''
Создайте собственный класс-исключение, который должен проверять содержимое списка 
на отсутствие элементов типа строка и булево. Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
'''


class Error:
    def __init__(self,*args):
        self.my_list = []

    def my_ls(self):

        while True:
            try:
                var =int(input('Введите значение и нажмите Enter - '))
                self.my_list.append(var)
                print(f'Список - {self.my_list} \n')
            except:
                print(f'Недопустимое значение - строка и булево')
                var_1 = input(f'Попробовать еще раз? Y/N ')

                if var_1 == 'Y' or var_1 == 'y':
                    print(my_except.my_ls())
                elif var_1 == 'N' or var_1 == 'n':
                    return  f'Вы вышли'
                else:
                    return f'Вы вышли'

my_except = Error(3)
print(my_except.my_ls())
