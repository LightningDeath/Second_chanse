
def conversion(ls):
    ls_2 = []
    for i in range(len(ls)):
        try:
            ls_2.append(bytes(ls[i], encoding='ascii'))
        except UnicodeEncodeError:
            print(f'Невозможно преобразовать! Слово "{ls[i]}" не будет преобразовано!')
    return ls_2


list_1 = ['attribute', 'класс', 'функция', 'type']
list_2 = conversion(list_1)
print(f'{list_1}\n{list_2}')
