'''
Реализовать проект расчета суммарного расхода ткани на 
производство одежды. Основная сущность (класс) этого 
проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) 
и рост (для костюма). Это могут быть обычные числа: V и H, 
соответственно. 
Для определения расхода ткани по каждому типу одежды использовать 
формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на 
практике полученные на этом уроке знания: реализовать абстрактные 
классы для основных классов проекта, проверить на практике 
работу декоратора @property.
'''


class Сlothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square_coat(self):
        return self.width / 6.5 + 0.5

    def square_jacket(self):
        return self.height * 2 + 0.3

    @property
    def square_all(self):
        return str(f'Общая площадь ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Сlothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь такани на пальто {self.square_c}'


class Jacket(Сlothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь такани на пальто {self.square_j}'


coat = Coat(3, 5)
jacket = Jacket(2, 5)
print(coat)
print(jacket)
print(coat.square_all)
print(jacket.square_all)
print(coat.square_coat())
print(jacket.square_jacket())
