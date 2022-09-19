""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """


n = 10
first = 0
second = 1
result = 0
i = 1
my_list = [0, 1]
while n > i:
    result = first + second
    first = second
    second = result
    i += 1
    my_list.append(result)
    print(result)
resNego = 0
my_nego_list = []
for i in range(1, len(my_list)):
    if (i % 2 == 0):
        resNego = my_list[i] * -1
    else:
        resNego = my_list[i]
    my_nego_list.append(resNego)

print(my_nego_list[::-1] + my_list)
