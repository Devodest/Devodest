""" Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.
[1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4] """


def exclude_duplicates(array):
    dictionary = {}
    for index in array:
        if not dictionary.get(index):
            dictionary[index] = 1
        else:
            dictionary[index] += 1
    for index in dictionary.keys():
        if dictionary[index] != 1:
            array = remove_values_from_list(array, index)
    return array


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


lst = [1, 1, 2, 3, 4, 5, 5, 1, 3, 5, 5]
result = exclude_duplicates(lst)
print(result)
