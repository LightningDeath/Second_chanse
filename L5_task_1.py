def ch_operator(op):
    #рекурсия для проверки правильности ввода оператора
    if op == '+' or op == '-' or op == '*' or op == '/' or op == '0':
        return op
    else:
        print('Вы ввели неправильный оператор! Попробуйте снова!')
        return ch_operator(input('Введите операцию (+, -, *, / или 0 для выхода): '))


def ch_vol(vol, word):
    # рекурсия для проверки правильности ввода числа
    try:
        v = int(vol)
    except ValueError:
        print('Вы ввели не число! Попробуйте еще раз!')
        return ch_vol(input(f'Введите {word} число: '), word)
    else:
        return v


def task_func(ope):
    # рекурсия для проведения определенного пользователем типа вычисления
    if ope == '0':  # если пользователь ввел 0 выход из рекурсии
        return print('Всего хорошего!')
    vol_1 = ch_vol(input('Введите первое число: '), 'первое')
    vol_2 = ch_vol(input('Введите второе число: '), 'второе')
    #  проведение вычислений в зависимости от выбора пользователя
    if ope == '-':
        print(f'Ваш результат: {vol_1 - vol_2}')
    elif ope == '+':
        print(f'Ваш результат: {vol_1 + vol_2}')
    elif ope == '*':
        print(f'Ваш результат: {vol_1 - vol_2}')
    elif ope == '/':
        try:
            print(f'Ваш результат: {vol_1 / vol_2}')
        except ZeroDivisionError:
            print('Делить на ноль нельзя! Попробуйте другие значения.')
            return task_func(ope)
    return task_func(ch_operator(input('Введите операцию (+, -, *, / или 0 для выхода): ')))


task_func(ch_operator(input('Введите операцию (+, -, *, / или 0 для выхода): ')))
