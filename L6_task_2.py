
def ch_vol(vol_1):
    # рекурсия для проверки правильности ввода числа
    try:
        v = int(vol_1)
    except ValueError:
        print('Вы ввели не число! Попробуйте еще раз!')
        return ch_vol(input(f'Введите число: '))
    else:
        return int(v)


a = -11
sp = list(a+(i+1) for i in range(21))
minimum_vol = ch_vol(input('Введите минимальное число: '))
maximum_vol = ch_vol(input('Введите максимальное число: '))
new_list = []
for i in sp:
    if minimum_vol <= int(sp[i]) <= maximum_vol:
        new_list.append(sp[i])
print(new_list)
