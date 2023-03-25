a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
try:
    print(f'Результат: {a/b}')
except ZeroDivisionError:
    print('Делить на ноль нельзя!')