# 1, 2, 3
'''Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста. Создать экземпляр и вывести информацию о человеке.
Доработать предыдущий класс, чтобы вся информация о человеке была доступна при вызове str над экземпляром.
Добавить метод greet, вызов которого будет выводить в консоль информацию о человеке в формате "Привет! Меня зовут Петров Василий, мне 12 лет".
Добавить поле grades, в котором будет храниться список оценок. Создать список учеников, заполняя оценки каждого случайными числами'''

from typing import List
from faker import Faker


class Person:
    def __init__(self, name, age, grades):
        self.age = age
        self.name = name
        self.__grades = grades

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def set_grades(self, grades: list[int]):
        self.__grades = grades

    def average_grade(self):
        average_grade = sum(self.__grades) / len(self.__grades)
        return self.name, self.average_grade

    def __greet__(self):
        return f"Привет! Меня зовут {self.name}, мне {self.age} лет. Мои оценки {self.__grades}"

list_students =[]
fake = Faker()
for i in range(10):
    list_students.append(Person(fake.name(), i, list(range(3, 7))))
for i in list_students:
    print(i.__greet__())

# 6
'''Создайте класс Point, экземпляры которого будут создаваться из координат x и y.'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point(3, 7))

# 9
class  Clock:
    def __init__(self):
        self._hours = 12
        self._minutes = 0
        self._seconds = 0

    def getHours(self):
        return self._hours

    def getMinutes(self):
        return self._minutes

    def getSeconds(self):
        return self._seconds

    def show(self):
        print("%d:%02d:%02d" % (self._hours, self._minutes, self._seconds))