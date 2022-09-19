"""
2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
1) с помощью математических формул нахождения корней квадратного уравнения
*2) с помощью дополнительных библиотек Python
 """
"""
 x 1,2 = − b ± D 2 a , D = b 2 − 4 ac , если дискриминант D ≥ 0
  Если D < 0, то решений уравнение не имеет """
a = 1
b = 2
c = 3
d = 0
firstX = None
secondX = None
d = b**2 - 4 * a * c


def descriminant(a, b, c):
    desc = (b**2 - (4 * a * c))
    if desc > 0:
        desc = desc ** 0.5
        firstX = (-b - desc) / (2 * a)
        secondX = (-b + desc) / (2 * a)
        return firstX, secondX
    elif desc == 0:
        desc = desc ** 0.5
        firstX = (-b)/(-2 * a)
        return firstX
    else:
        return -1


desc = descriminant(a, b, c)
if desc == -1:
    print(f'Корней с отрицательным D: {desc} нет')
else:
    print(desc)