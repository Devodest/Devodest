
""" 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
Ответ записать в файл. """


""" firstNumber = 126
secondNumber = 70
count = firstNumber * secondNumber

while firstNumber != secondNumber:
    if firstNumber > secondNumber: firstNumber -= secondNumber
    else: secondNumber -= firstNumber
print(count/secondNumber) """

import math

num_1 = 126
num_2 = 70
print(math.lcm(num_1, num_2))

with open('file.txt', 'w') as f:
    f.write(str(math.lcm(num_1, num_2)))