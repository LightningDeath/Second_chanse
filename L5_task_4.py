def ch_vol(vol):
    # рекурсия для проверки правильности ввода числа
    try:
        v = int(vol)
    except ValueError:
        print('Вы ввели не число! Попробуйте еще раз!')
        return ch_vol(input(f'Введите число: '))
    else:
        return int(v)


def task_func(n, b=1, a=1, summa=1):
    # рекурсия подсчета последовательности 1 -0.5 0.25 -0.125 и т.д.
    if b == n:
        return print(f'Результат подсчета суммы последовательности: {summa}')
    elif b % 2 == 0:
        summa += a/2
        a = a / 2
        return task_func(n, b+1, a, summa)
    else:
        summa -= a/2
        a = a / 2
        return task_func(n, b+1, a, summa)


a_1 = ch_vol(input('Введите количество элементов последовательности: '))
task_func(a_1)
