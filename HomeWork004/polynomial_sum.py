""" Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов. """

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

indexes_reverse = {v: k for k, v in indexes.items()}


def int_to_superscript(num: int):
    degrees = ""
    temp = str(num)
    for item in temp:
        degrees += indexes[item] or ""
    return degrees


def superscript_to_int(superscript: str):
    return indexes_reverse[superscript]


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        string = f.readline()
        f.close()
    return string


def create_file_with_polynomial(string):
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(string)


def string_to_dict(string: str):
    array_part = string.split(' + ')
    dict_numbers = {}
    for part in array_part:
        if 'x' in part:
            factor, degree = part.split('x')
            if degree == '':
                degree = int_to_superscript(1)
        else:
            factor, degree = part, int_to_superscript(0)
        if factor == '':
            factor = 1
        dict_numbers[int(superscript_to_int(degree))] = int(factor)
    return dict_numbers


first_string = read_file('first.txt')
second_string = read_file('second.txt')

f_result = string_to_dict(first_string)

s_result = string_to_dict(second_string)

array_degrees = list(f_result.keys()) + list(s_result.keys())

array_degrees = list(dict.fromkeys(array_degrees))
array_degrees.sort(reverse=True)

result_array = []
for d in array_degrees:

    if d in f_result.keys() and d in s_result.keys():
        result_array.append(f_result[d] + s_result[d])
    elif d in f_result.keys():
        result_array.append(f_result[d])
    elif d in s_result.keys():
        result_array.append(s_result[d])

k = len(result_array) - 1
result = 0
new_list = []

for i in range(0, len(result_array)):
    result = result_array[i]
    if result == 1:
        if k == 1:
            new_list.append(f'x')
        elif k == 0:
            new_list.append(f'1')
        else:
            new_list.append(f'x{int_to_superscript(k)}')
    elif result > 1 and k == 1:
        new_list.append(f'{result}x')
    elif result > 1 and k > 1:
        new_list.append(f'{result}x{int_to_superscript(k)}')
    elif result > 1:
        new_list.append(f'{result}')

    k -= 1

result = ' + '.join(new_list)

create_file_with_polynomial(result)
