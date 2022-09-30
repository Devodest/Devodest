""" 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

    Примеры:

    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90
 """

""" num_1 = int(input('Ввведите число 1 - '))
num_2 = int(input('Ввведите число 2 - '))
num_3 = int(input('Ввведите число 3 - '))
num_4 = int(input('Ввведите число 4 - '))
num_5 = int(input('Ввведите число 5 - '))

max = 0
if num_1 > max:
    max = num_1
if num_2 > max:
    max = num_2
if num_3 > max:
    max = num_3
if num_4 > max:
    max = num_4
if num_5 > max:
    max = num_5

print(max) """

"""
# range(5) -> [0, 1, 2, 3, 4]
# range(5, 16) -> [5, 6, 7 ..., 13, 14, 15]
# range(1, 11, 2) -> [1, 3, 5, 7, 9]
my_list = []
for i in range(5):
    num = int(input('--> '))
    my_list.append(num)
print(my_list) """

""" my_list = [3, 5, 1, 2, 8]
maxx = my_list[0]
for item in my_list:
    if item > maxx:
        maxx = item
print(maxx) """

""" my_list = [3, 5, 1, 2, 8]
maxx = my_list[0]
for i in range(len(my_list)):
    if my_list[i] > maxx:
        maxx = i

print(maxx) """

# print(max(my_list))

""" 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

    *Примеры:*

    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

    *Примеры:*

    - 6,78 -> 7
    - 5 -> нет
    - 0,34 -> 3
3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30)
 """
# 1

""" n = int(input('Введите число N: '))
for i in range(-n, n + 1):
    print(f'* {i} *') """


# 2

""" number = input("Input number: ")

print(number.split(',')[1][0])
 """

""" number = float(input("Input number: "))
number *= 10 
number = int(number)
print(number % 10) """


# 3

""" num_1 = int(input('Введите число'))

if ((num_1 % 5 == 0) and (num_1 % 10 == 0)) or ((num_1 % 15 == 0) and (num_1 % 30 != 0)):
    print("true")
else:
    print("false") """
