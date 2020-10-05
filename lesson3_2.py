'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


name = input("Введите Ваше имя: ")
surname = input("Введите Вашу фамилию: ")
year = int(input("Введите Ваш год рождения: "))
city = input("Введите город проживания: ")
email = input("Введите email: ")
telefon = int(input("Введите номер телефона: "))
'''

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Шевцов', name='Артем', year='1987', city='Москва', email='tim@mail.ru', telephone='8-920-45-56-56'))