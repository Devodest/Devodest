# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
#
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

expression = '2 + 2 * 4 / 2 * 2'.split(' ')
index = 0
summa = None
for i in range(len(expression)):
    if expression[i].isdigit():
        expression[i] = int(expression[i])

op_1 = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y}
op_2 = {'*': lambda x, y: x * y,
        '/': lambda x, y: x / y}

while '*' in expression or '/' in expression:
    if expression[index] in op_2:
        temp = op_2[expression[index]](expression[index - 1], expression[index + 1])
        del expression[index - 1:index + 2]
        expression.insert(index - 1, temp)
        index = 0
    else:
        index += 1
while '+' in expression or '-' in expression:
    if expression[index] in op_1:
        temp = op_1[expression[index]](expression[index - 1], expression[index + 1])
        del expression[index - 1:index + 2]
        expression.insert(index - 1, temp)
        index = 0
    else:
        index += 1
print(expression)
