def sum(x, y):
    # функция создания таблицы умножения чисел где x - строки, y - солбцы
    n = y                                                     # задаем дополнительный счетчик
    my_list = [i + 1 for i in range(y)]                       # создаем первую строку, по которой будем создавать всю таблицу
    # инициируем цикл добавления элементов в список
    for i in range(x - 1):                                    # х - 1, т.к. у нас есть уже первая строка
        my_list.append(my_list[i] + 1)             # Добавляем первое значение в начале следующей строки равное следующему столбцу
        for j in range(y - 1):                                # y - 1, т.к. у нас есть первый элемент строки
            my_list.append(my_list[j + 1] + my_list[i + n])   # складываем числа столбца с числом строки
        n += y - 1                                        # увеличиваем дополнительный счетчик, чтобы начать со следующей строки
    return my_list


def multiplication(x, y):
    n = y
    my_list = [i + 1 for i in range(y)]
    for i in range(x - 1):
        my_list.append(my_list[i] + 1)
        for j in range(y - 1):
            my_list.append(my_list[j + 1] * my_list[i + n])
        n += y - 1
    return my_list


def division(x, y):
    n = y
    my_list = [i + 1 for i in range(y)]
    for i in range(x - 1):
        my_list.append(my_list[i] + 1)
        for j in range(y - 1):
            my_list.append(my_list[j + 1] + my_list[i + n])
        n += y - 1
    return my_list


def subtract(x, y):
    n = y
    my_list = [i + 1 for i in range(y)]
    for i in range(x - 1):
        my_list.append(my_list[i] + 1)
        for j in range(y - 1):
            my_list.append(my_list[i + n] - my_list[j + 1])
        n += y - 1
    return my_list
