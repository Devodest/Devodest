"""  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
между максимальным и минимальным значением дробной части элементов.

Пример:
- [1.1, 1.2, 3.1, 10.01] => 0.19 """
from math import floor


origin_list = [1.1, 1.2, 3.1, 10.01]
new_list = list(map(lambda num: round(num - floor(num), 2), origin_list))
res = max(new_list) - min(new_list)
print(f'Максимальный элемент {max(new_list)} - минимальный элемент {min(new_list)} = {res}')
