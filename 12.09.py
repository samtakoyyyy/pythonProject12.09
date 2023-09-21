"""
Выбрать (в виде списка) из текста все слова без повторений, содержащие 3 и более одинаковые буквы.
Разделителями слов считаются любые символы, отличные от букв А-Я, A-Z и цифр.
"""
import random
import re
from abc import ABC, abstractmethod


#регулярка https://habr.com/ru/articles/349860/


#Функция проверки подходит ли слово под критерий
def how_many(word):
    for c in set(word):
        if word.count(c) >= 3:
            return True
    return False

#фильтр слов для выборки
def filter(words):
    return [word for word in words if how_many(word)]

text = "hf hgs , s d, s  s ds ds, ds goodo aaa  aaa ааа \n ыыыы "
print(text)
#регулярка для выборки слов
words = re.findall(r'\b\w{3,}\b', text)
print(words)
words = list(set(words))
print(words)

print(filter(words))


"""(*) Для переданного двумерного массива определить, образуют ли его элементы 
упорядоченную последовательность при просмотре элементов в следующем порядке: рис 1 """

def check_borders(matrix, i, j):
    return 0 <= i <= len(matrix)-1 and 0 <= j <= len(matrix[0])-1

matrix = [
    [1,  2,   3,   4],
    [8,  7,   6,   5],
    [9,  10,  11,  12],
    [16, 15,  14,  13]
          ]

def check_matrix(matrix):
    direction = 1
    i, j = 0, 0

    prev = matrix[i][j]

    i, j = i, j+direction
    s = matrix[i][j] - prev

    if s not in [1, -1]:
        return False

    while check_borders(matrix, i, j):
        #print(matrix[i][j])
        if matrix[i][j] - prev != s:
            return False
        prev = matrix[i][j]
        if not check_borders(matrix, i, j+direction):
            direction*=-1
            i+=1
        else:
            j+=direction
    return True

print(check_matrix(matrix))


#Есть человек сдавший егэ, у него есть фио балл русского балл математики и физики отсортировать людей
#сначала по суммарному, потом по физикуе, матему, русскому

class Entrant:
    def __init__(self, fio, rus, mat, phy):
        self.fio = fio
        self.rus = rus
        self.mat = mat
        self.phy = phy

    def sum(self):
        return self.mat+self.rus+self.phy

#Род класс
class Univercity(ABC):
    def __init__(self,border_phy,border_rus,border_mat):
        self.border_phy = border_phy
        self.border_rus = border_rus
        self.border_mat = border_mat

    def is_valid_entrant(self, phy, rus, mat):
        return self.border_phy <= phy and self.border_rus <= rus and self.border_mat <= mat


#super - ссылка на род класс
class VSU(Univercity):
    def __init__(self, border_phy, border_rus, border_mat):
        super().__init__(border_phy, border_rus, border_mat)
    def is_valid_entrant(self, phy, rus, mat):
        return super().is_valid_entrant(phy, rus, mat)






def generate_entrant(i):
    return Entrant(
        "Entrant_"+str(i),
        30+random.randint(0, 70),
        30+random.randint(0, 70),
        30+random.randint(0, 70)
    )
#десериализация класса - это процесс маппинга по полям

border_phy = 42
border_rus = 36
border_mat = 30

v = VSU(70, 30, 30)

entrants = [generate_entrant(i) for i in range(10)]

print('\n'.join(str(e.__dict__) for e in entrants))
print("_______")
#фИЛЬТРУЕМ ЛЮДЕЙ ПО ПОРОГУ
entrants = [e for e in entrants if v.is_valid_entrant(e.phy, e.rus, e.mat)]
print("++++++++")
print('\n'.join(str(e.__dict__) for e in entrants))
print("++++++++")
entrants = sorted(entrants, key= lambda e: (e.sum(), e.phy, e.mat, e.rus))
print('\n'.join(str(e.__dict__) for e in entrants))

#массив можно перевернуть 2мя способами [::-1] или через .reverse()
print("_______")

entrants.reverse()
print('\n'.join(str(e.__dict__) for e in entrants))

#доп задание! выбрать N самых крутых абитуриентов
N=5
print("_______")

entrants = entrants[0:N] # срезаем сначала
print('\n'.join(str(e.__dict__) for e in entrants))
#Чтобы срезать с конца, мы пишем [N:]