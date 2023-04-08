# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
#
# П.С. попытайтесь добиться вывода информации о сотруднике также через перегрузку str
# str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
import Chek_input_vol as C


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'Сотрудник: {self.surname} {self.name} {self.position}'

    def get_total_income(self):
        return f'\nДоход сотрудника с учетом премии: {self._income["wage"] + self._income["bonus"]}'

    def __str__(self):
        return f'Сотрудник: {self.surname} {self.name} {self.position}' \
               f'\nДоход сотрудника с учетом премии: {self._income["wage"] + self._income["bonus"]}'


inc = {}
name_1 = input('Введите имя сотрудника: ')
surname_1 = input('Введите фамилию сотрудника: ')
position_1 = input('Введите должность сотрудника: ')
inc['wage'] = C.ch_num_f(input('Введите оклад сотрудника: '), 'оклад сотрудника')
inc['bonus'] = C.ch_num_f(input('Введите бонус сотрудника: '), 'бонус сотрудника')
print(inc)
pos = Position(name_1, surname_1, position_1, inc)
print(pos.name, pos.surname, pos.position, pos._income)
print(pos.get_full_name(), pos.get_total_income())
print(pos)
