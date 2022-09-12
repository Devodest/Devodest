""" 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
['65h34q', 'sdg634d', '147jnbv']
"7" """


list_1 = ['qwe', 'qwe', 7]
number = input()
number_bool = False
for i in list_1:
    if i.find(number) != -1:
        print(i)
        number_bool = True
if not number_bool:
    print('No')


array_of_string = ['65h34q', 'sdg634d', '147jnbv']
number = int(input("Введите число: "))

for i in array_of_string:
    for j in i:
        if j.isdigit() and int(j) == number:
            print('Да, есть')
