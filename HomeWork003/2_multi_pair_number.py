""" Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]   """

from math import ceil


my_list = [2, 3, 4, 5, 6]
res_list = []
for i in range(0, ceil(len(my_list)/2)):
    first = i
    last = -(i+1)
    res = my_list[first] * my_list[last]
    print(f'{my_list[i]} * {my_list[last]} = {res}')
    print("_______________________")
    res_list.append(res)
print('\n\n')
print('Результируюзий массив', res_list)
