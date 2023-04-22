
my_list = ['разработка', 'администрирование', 'protocol', 'standard']
my_list_encode = []
my_list_decode = []

for i in range(len(my_list)):
    my_list_encode.append(my_list[i].encode())
    my_list_decode.append(my_list_encode[i].decode())

print(f'оригинальный список слов: {my_list}\n'
      f'преобразованный в байты: {my_list_encode}\n'
      f'обратное преобразование: {my_list_decode}')
