'''
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''



class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} поехал'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'{self.name} скорость составляет {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость городского автомобиля {self.name} на данный момент {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость {self.name} выше, чем разрешается ездить в городе'
        else:
            return f'Скорость {self.name} с которой можно ездить по городу'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочего автомобиля {self.name} на данный момент {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} выше, чем разрешается ездить на рабочем автомобиле'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


kia = SportCar(80, 'Серый', 'KIA', False)
smart = TownCar(60, 'Черный', 'Smart', False)
hyundai = WorkCar(100, 'Синий', 'Hyundai', False)
ford = PoliceCar(120, 'Белый',  'Ford', True)
print(hyundai.turn_left())
print(f'{smart.turn_left()}, а {ford.turn_right()}')
print(f'{hyundai.name} {hyundai.color}')
print(f'{kia.name} из полиции? {kia.is_police}')
print(f'{ford.name} полицейский автомобиль? {ford.is_police}')
print(kia.show_speed())
print(smart.show_speed())
print(ford.police())
print(hyundai.show_speed())