import Chek_input_vol as C


class Mydesk:
    def __init__(self, my_attr, st):
        self.my_attr = my_attr
        self.st = st

    def __set__(self, instance, value):
        if value.isdigit():
            return self.__set__(instance, input('Введены не корректные данные о сотруднике!\n'
                                                f'Введите {self.st} сотрудника: '))
        else:
            instance.__dict__[self.my_attr] = value


class Worker:
    name = Mydesk('name', 'имя')
    surname = Mydesk('surname', 'фамилию')
    position = Mydesk('position', 'должность')

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
        return f'Сотрудник: {self.surname} {self.name} {self.position}\n' \
               f'Доход сотрудника с учетом премии: {Mydesk("_income", "wage") + self._income["bonus"]}'


inc = {}
name_1 = input('Введите имя сотрудника: ')
surname_1 = input('Введите фамилию сотрудника: ')
position_1 = input('Введите должность сотрудника: ')
inc['wage'] = C.ch_num_i(input('Введите оклад сотрудника: '), 'оклад сотрудника')
inc['bonus'] = C.ch_num_i(input('Введите бонус сотрудника: '), 'бонус сотрудника')
pos = Position(name_1, surname_1, position_1, inc)
print(pos)
