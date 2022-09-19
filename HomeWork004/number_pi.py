""" Вычислить число c заданной точностью d
Пример:

при $d = 0.001, π = 3.141 """
import math


def get_precision(f):
    str_f = str(f)
    if '.' not in str_f:
        raise ValueError('Number should be fractional.')
    return len(str_f[str_f.index('.') + 1:])


pi = math.pi
accuracy = 0.001
accuracy = get_precision(accuracy)
print(pi)
print(round(pi, accuracy))
