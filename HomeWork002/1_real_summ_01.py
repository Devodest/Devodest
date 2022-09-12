""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 0,56 -> 11 """


number = input('Введите вещественное число ')
number = number.split(',')
whole_part = int(number[0])
fractional_part = int(number[1])
mult = 0
while (whole_part != 0):
    mult = mult + (whole_part % 10)
    whole_part //= 10
while (fractional_part != 0):
    mult = mult + (fractional_part % 10)
    fractional_part //= 10
print(f'Сумма цифр = {mult}' )