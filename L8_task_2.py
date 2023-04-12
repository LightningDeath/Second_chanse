import json

from Chek_input_vol import *


def write_order_to_jonson(item, quantity, price, buyer, date):
    order_dict = {'orders': [
        {
            'item': str(item),
            'quantity': str(quantity),
            'price': str(price),
            'buyer': buyer,
            'date': date
        }
    ]
    }
    try:  # проверка пустой ли файл
        with open('orders.json') as o_d:  # если не пустой, то получаем данные и добавляем свои
            o_dict = json.load(o_d)
        o_dict['orders'].append(order_dict['orders'][0])
        with open('orders.json', 'w') as t:
            t.write(json.dumps(o_dict, indent=4, ensure_ascii=False))
    except json.JSONDecodeError:  # если пустой записываем свои данные
        with open('orders.json', 'w') as t:
            t.write(json.dumps(order_dict, indent=4, ensure_ascii=False))


def ch_user_choose():
    vol = ch_num_i(input('Введите 1 для ввода следующего заказа или 0 для выхода: '),
                   '1 для ввода следующего заказа или 0 для выхода')
    if 1 != vol != 0:
        print('Вы ввели не верную цифру! Попробуйте ещё раз!')
        return ch_user_choose()
    else:
        return vol


x = 1
while x != 0:  # цикл для ввода пользователем нужного ему количества заказов
    it_name = ch_str(input('Введите название товара: '), 'название товара')
    quan = ch_num_i(input('Введите количество товара: '), 'количество товара')
    pr = ch_num_f(input('Введите стоимость товара: '), 'стоимость товара')
    buy = ch_str(input('Введите ФИО покупателя: '), 'ФИО покупателя')
    d = ch_str(input('Введите дату заказа(дд.мм.гг): '), 'дату заказа(дд.мм.гг)')
    x = ch_user_choose()
    write_order_to_jonson(it_name, quan, pr, buy, d)
