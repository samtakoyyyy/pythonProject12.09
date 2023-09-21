#Создать абстрактный класс машина (поля объем движка, кол-во цилиндров, диаметр колес, вес, макс скорость).
# функцию доедет ли машина на фул скорости за  N минут заданное расстояние.
# Так же наследовать от него парочку классов Хонда цивик,  мазда сх5
# и проверить сможет ли одна из машин доехать
# За 30 мин
# 80 км
import random
from abc import ABC

class Cars(ABC):
    def __init__(self, name, v, c, d, p, maxv, t, s):
        self.name = name
        self.v = v
        self.c = c
        self.d = d
        self.p = p
        self.maxv = maxv
        self.s = s
        self.t = t

    def way(self):
        if self.t == self.s / self.maxv:
            return True
        else:
            return False

class HondaCivic(Cars):
    def __init__(self,name, v, c, d, p, maxv, t, s):
        super().__init__(name, v, c, d, p, maxv, t, s)


class MazdaCX5(Cars):
    def __init__(self, name, v, c, d, p, maxv, t, s):
        super().__init__(name, v, c, d, p, maxv, t, s)


def generate_cars(i):
    return Cars(
        " Car_" + str(i + 1),
        random.randint(2, 5),
        random.randint(5, 10),
        random.randint(40, 50),
        random.randint(1500, 2000),
        random.randint(100, 300),
        random.randint(5, 30),
        random.randint(100, 1000)
    )

cars = [generate_cars(i) for i in range(10)]

print('\n'.join(str(e.__dict__) for e in cars))
m = MazdaCX5(2, 6, 7, 40, 1670, 260, 8, 200)