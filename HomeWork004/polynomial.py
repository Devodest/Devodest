""" Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:

k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 """
import random

indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }


def degree(num: int):
    degrees = ""
    temp = str(num)
    for item in temp:
        degrees += indexes[item] or ""
    return degrees


def get_random_array(polynomial_coefficient):
    my_list = []
    for index in range(0, polynomial_coefficient + 1):
        my_list.append(random.randrange(1, 4))
    return my_list


def create_file_with_polynomial(string):
    with open('second.txt', 'w', encoding='utf-8') as file:
        file.write(string)


k = 5
result = 0
new_list = []
array = get_random_array(k)

for i in range(0, len(array)):
    result = array[i]
    if result == 1:
        if k == 1:
            new_list.append(f'x')
        elif k == 0:
            new_list.append(f'1')
        else:
            new_list.append(f'x{degree(k)}')
    elif result > 1 and k == 1:
        new_list.append(f'{result}x')
    elif result > 1 and k > 1:
        new_list.append(f'{result}x{degree(k)}')
    elif result > 1:
        new_list.append(f'{result}')

    k -= 1

result = ' + '.join(new_list)

create_file_with_polynomial(result)


