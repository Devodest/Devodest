""" 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
В качестве символа-разделителя используйте пробел.
 """



string = input('Введите строку из набора чисел ').split(' ')
print (string)
numbers = []
range = range(len(string))
for i in range:
    numbers.append(int(string[i]))
print(f' Максимальный элемент: {max(numbers)} \n Минимальный эелемент {min(numbers)}')
