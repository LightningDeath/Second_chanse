
list_1 = ['class', 'function', 'method']
list_2 = []

for i in range(len(list_1)):
    list_2.append(bytes(list_1[i], encoding='utf-8'))

for k in range(len(list_1)):
    print(f'Слово № {k + 1}: {list_1[k]}', '\n'
          f'тип данных слова № {k + 1}: {type(list_1[k])}')

for j in range(len(list_2)):
    print(f'Слово № {j + 1} в байтовом формате: {list_2[j]}', '\n'
          f'тип данных слова № {j + 1}: {type(list_2[j])}')
