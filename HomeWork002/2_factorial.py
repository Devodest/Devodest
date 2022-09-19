""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример: """

number = int(input('Введите число N: '))
fact = 1
for i in range(1, number + 1):
    fact = fact * i
    print(fact, end=' ')