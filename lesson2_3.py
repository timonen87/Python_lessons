
list_season = ['winter', 'spring', 'summer', 'autumn' ]
dict_season = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц "))
if month == 1 or month == 2 or month == 12:
    print(dict_season.get(1))
    print(list_season[0])
elif month == 3 or month == 4 or month == 5:
    print(dict_season.get(2))
    print(list_season[1])
elif month == 6 or month == 7 or month == 8:
    print(dict_season.get(3))
    print(list_season[2])
elif month == 9 or month == 10 or month == 10:
    print(dict_season.get(4))
    print(list_season[3])
else:
    print("Такого месяца не существует!")


