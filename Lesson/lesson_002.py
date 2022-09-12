""" 1. Напишите программу, которая принимает на вход число N и
выдаёт последовательность из N членов.

*Пример:*
- Для N = 5: 1, -3, 9, -27, 81 """

""" n = int(input("Введите число n "))
i = 1
x = 1
while i < n:
    x = x * (-3)
    i += 1
    print(x)
else:
    print('END!')
 """

n = int(input())

value = 1
for _ in range(n):
    print(value, end=' ')
    value *= -3

""" number = int(input('Введите число:'))
numbers = [1]

for i in range(number-1):
    num = (numbers[i]* -3)
    numbers.append(num)

print(numbers)
 """
""" 2. Для натурального n создать последовательности 3n + 1.

*Пример:*
- Для n = 6:
1: 4,
2: 7,
3: 10,
4: 13,
5: 16,
6: 19 """

""" number = int(input('Введите число: '))
numbers = []
for i in range(1, number + 1):
    num = (3 * i + 1)
    numbers.append(num)
    print(f'{i}: {num}') """

""" n = int(input('Введите число n '))
i=0
while i <= n:
    x = 3 * i + 1
    i+=1
    print(x)
 """
""" Напишите программу, в которой пользователь будет задавать две
строки, а программа - определять количество вхождений одной строки в другой.

*Пример:*
'Я люблю Питон!'
'лю' """

""" words = 'Я люблю Питон Люблю люблю'
words = words.lower()
print(f'сочетание "лю" встречается {words.count("лю")} раз') """

string = input('Введите строку')
string2 = input('Введите искомую подстроку')
