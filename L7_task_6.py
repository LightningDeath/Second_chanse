# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется
# любая операция, у которой ровно два аргумента, как, например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
from Chek_input_vol import ch_num_i, ch_sign
import L7_task_6_def as Def_task


class Chart:

    def print_operation_table(self, num_rows, num_colums, chart_create_1, st):
        self.ch_cr = chart_create_1
        self.n_r = num_rows
        self.n_c = num_colums
        self.st = st
        k = 0
        print(f'Таблица операции {st}:')
        for i in range(self.n_r):
            for j in range(self.n_c):
                print(self.ch_cr[j + k], end=' ')
            k += y
            print()


sign = ch_sign(input('Введите вид операции: '))
x = ch_num_i(input('Введите количество строк таблицы: '), 'количество строк таблицы')
y = ch_num_i(input('Введите количество столбцов таблицы: '), 'количество столбцов таблицы')
c = Chart()
if sign == '*':
    c.print_operation_table(x, y, Def_task.multiplication(x, y), 'умножения')
elif sign == '/':
    c.print_operation_table(x, y, Def_task.division(x, y), 'деления')
elif sign == '+':
    c.print_operation_table(x, y, Def_task.sum(x, y), 'сложения')
elif sign == '-':
    c.print_operation_table(x, y, Def_task.subtract(x, y), 'вычитания')
