""" Реализуйте алгоритм перемешивания списка. """

import random


range = list(range(10))
# random.shuffle(range)
# print(range)


for i in range:
    j = random.randint(0, len(range)-1)
    range[i], range[j] = range[j], range[i]

print(range)
