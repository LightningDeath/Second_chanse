def ch_vol(vol_1):
    # рекурсия для проверки правильности ввода числа
    try:
        v = int(vol_1)
    except ValueError:
        print('Вы ввели не число! Попробуйте еще раз!')
        return ch_vol(input(f'Введите число: '))
    else:
        return int(v)


a1 = ch_vol(input('ВВедите первое число: '))
b = ch_vol(input('Введите число на которе увеличить: '))
n = ch_vol(input('Введите количество элементов: '))
sp = []
for i in range(n):
    s_1 = sp.append(a1 + i * b)
print(sp)
