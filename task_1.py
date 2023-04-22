

def converting(my_list):
    decoding_list = []
    for i in range(len(my_list)):
        d = my_list[i]
        decoding_list.append(d.encode('unicode_escape').decode())
    return decoding_list


s = ['разработка', 'сокет', 'декоратор']
a = converting(s)
for k in range(len(s)):
    print(f'Слово № {k + 1}: {s[k]}', '\n'
          f'тип данных слова № {k + 1}: {type(s[k])}')
for j in range(len(a)):
    print(f'Слово № {j + 1} в формате кодовых точек: {a[j]}', '\n'
          f'тип данных слова № {j + 1}: {type(a[j])}')
