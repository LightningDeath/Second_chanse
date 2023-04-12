import os
import re
import csv


def get_data():
    content = os.listdir()  # получаем список файлов в директории
    for i in os.listdir():  # цикл для отсеивания файлов не формата txt
        k = i.split('.')
        if k[1] != 'txt':
            content.remove(i)
    my_list = []
    for i in content:  # цикл получения нужных данных из каждого файла txt
        with open(i) as f:
            data = f.read()
            os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
            os_name = re.compile(r'Название ОС:\s*\S*\s*\S*\s*\S*\s*\S*')
            os_code = re.compile(r'Код продукта:\s*\S*')
            os_type = re.compile(r'Тип системы:\s*\S*\s*\S*')
            os_name_list = [os_prod_reg.findall(data)[0].split()[2], ' '.join(os_name.findall(data)[0].split()[2:6]),
                            os_code.findall(data)[0].split()[2], ' '.join(os_type.findall(data)[0].split()[2:4])]
            my_list.append(os_name_list)
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for i in range(len(content)):  # цикл записи полученных данных в отдельные файлы
        with open(f'main_data_{i + 1}.bat', 'w') as f:
            f.write(f'{str(i + 1)}, ')
            f.write(', '.join(my_list[i]))
    return main_data


def write_to_csv(a):
    head = get_data()
    with open(a, 'w') as b:  # записываем шапку в файл
        c = csv.writer(b)
        c.writerow(head)
    content = os.listdir()
    for i in os.listdir():  # цикл для получения списка файлов из которых будем считывать данные
        k = i.split('.')
        if k[1] != 'bat':
            content.remove(i)
    for i in content:   # цикл считывания данных и записи в файл csv
        with open(i, 'r') as f:
            data = [f.read()]
        with open(a, 'a') as f_csv:
            data_csv = csv.writer(f_csv)
            data_csv.writerow(data)


write_to_csv('data_csv.csv')

with open('data_csv.csv', 'r') as fa:
    print(fa.read())
