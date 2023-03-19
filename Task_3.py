def user_data(name, last_n, date, city, email, phone):
    print(f'{name} {last_n} {date} года рождения, проживает в городе {city}, email: {email}, телефон: {phone}')
    return


n = input('Введите имя пользователя: ')
l = input('Введите фамилию пользователя: ')
d = input('Введите год рождения пользователя: ')
c = input('Введите город рождения пользователя: ')
e = input('Введите email пользователя: ')
p = input('Введите телефон пользователя: ')

user_data(name=n, last_n=l, date=d, city=c, email=e, phone=p)
