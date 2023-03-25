def my_func_1(a, b, c):
    d = (a, b, c)
    d = sorted(d)
    s = d[2]+d[1]
    return s


def my_func_2(a, b, c):
    d = (a, b, c)
    if d[0] > d[1] > d[2] and d[0] > d[2]:
        s = d[0] + d[1]
    elif d[0] > d[1]:
        s = d[0] + d[2]
    else:
        s = d[2]+d[1]
    return s


vol_1 = int(input('Введите первое число: '))
vol_2 = int(input('Введите второе число: '))
vol_3 = int(input('Введите третье число: '))
print('Функция sort:', my_func_1(vol_1, vol_2, vol_3))
print('Без функции sort:', my_func_2(vol_1, vol_2, vol_3))
