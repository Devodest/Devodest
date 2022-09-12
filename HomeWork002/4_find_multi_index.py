""" Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных пользователем через пробел позициях. """


n = int(input('Введите число n:  '))
index = input('Введите позиции элементов через пробел: ')
index = index.split(' ')

result = None
range = range(-n, n+1)
for idx in index:
    idx = int(idx)
    if(result == None):
        result = range[idx]
    else:
        result = result * range[idx]

print(result)