
from Chek_input_vol import ch_num_i
from random import *


class Matrix:
    my_dict = {}
    my_matrix_1 = []
    my_matrix_2 = []

    def __init__(self, list_1, strok, stolb):
        self.list_1 = list_1
        self.strok = strok
        self.stolb = stolb
        for i in range(strok):
            self.my_matrix_1.append(list_1[i])
        for i in range(strok):
            self.my_matrix_2.append(list_1[i + strok])
        self.my_dict[0], self.my_dict[1] = self.my_matrix_1, self.my_matrix_2

    def __str__(self):
        for i in range(2):
            print(f'Матрица №{i + 1}: ')
            for j in range(strok):
                print(*self.my_dict[i][j])
            print()
        return ''

    def __add__(self, other):
        for i in range(strok):
            for j in range(stolb):
                self.my_matrix_1[i][j] += self.my_matrix_2[i][j]
        print('Сложением двух матриц является матрица: ')
        for i in range(strok):
            print(*self.my_matrix_1[i])
        return '\nРабота программы завершена'


strok = ch_num_i(input('Введите количество строк матриц: '), 'количество строк матриц')
stolb = ch_num_i(input('Введите количество столбцов матриц: '), 'количество столбцов матриц')
my_list_1 = []
for a in range(2):
    for b in range(strok):
        m_list = [randint(0, 100) for i in range(stolb)]
        my_list_1.append(m_list)

m = Matrix(my_list_1, strok, stolb)
print(m)
print(m + m)
