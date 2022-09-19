""" 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел. """



import time

number = time.time()
number = (round(number, 2) * 100 % 100)
number = str(number)
number = number.split('.')
print(number[0])


