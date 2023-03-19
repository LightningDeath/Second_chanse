a = int(input('длинна массива: '))
b = int(input('Число, которое надо найти: '))
list_1 = list()
for i in range(a):
    list_1.append(i+1)
c = 0
for i in range(len(list_1)):
    if list_1[i] == b:
        c = c+1
print(list_1)
print(b)
print(f'->{c}')
