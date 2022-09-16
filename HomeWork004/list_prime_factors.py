""" Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"20" -> [2, 2, 5] """


def Factor(n):
    i = 2
    while n % i != 0:
        i += 1
    lst.append(i)
    if n / i > 1:
        Factor(n / i)


number = 20
lst = []
Factor(number)
print(lst)
