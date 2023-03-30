def ch_vol(vol_1):
    # рекурсия для проверки правильности ввода числа
    try:
        v = int(vol_1)
    except ValueError:
        print('Вы ввели не число! Попробуйте еще раз!')
        return ch_vol(input(f'Введите число: '))
    else:
        return int(v)


def task_func(n, i=1, summa=0):
    # рекурсия подсчета суммы последовательности
    # чисел с длинной заданной пользователем
    if n == 0:
        return n
    if n == i:
        summa += i
        return summa
    else:
        summa += i
        i += 1
        return task_func(n, i, summa)


def str_build(n, b=''):
    # рекурсия создания строки
    # в зависимости от выбранного пользователем
    # количества элементов
    if n == 0:
        return ''.join(reversed(b[:-1]))  # разворот строки срезом строки
    else:
        if n >= 10:  # если больше 10 символов, то делаем короткую строку для лучшей читабельности
            b = '1+2+3+...+' + str(n)
            return b
        else:
            b += str(n) + '+'  # создание строки в зависимости от количества элементов заданных пользователем
            return str_build(n-1, b)


vol = ch_vol(input('Введите любое натуральное число: '))
if vol == 0:
    print(f'{vol} = {vol}({vol}+1)/2')
elif task_func(int(vol)) == vol * (vol + 1) / 2:
    print(f'{str_build(vol)} = {vol}({vol}+1)/2')
else:
    print('Равенство не выполняется!!!!!')
