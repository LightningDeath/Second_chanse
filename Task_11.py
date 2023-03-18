s = int(input('Введите сумму загаданных чисел: '))
p = int(input('Введите произведение загаданных чисел: '))
for i in range(s):
    for j in range(p):
        if s == i + j and p == i * j:
            print(f'Загаданные Вами числа: {i}, {j}')
            break