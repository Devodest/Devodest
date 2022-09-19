""" Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму. """


number = int(input('Введите число k: '))

res = 0
sum = 0
for i in range(1, number+1):
    res += (1+1/i)**i
    sum = sum + res

print(round(sum, 2))
