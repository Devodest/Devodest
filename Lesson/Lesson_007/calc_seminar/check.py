import math_f


def check(data):
    # if data[1] == '+':
    #     return math_f.summa(data[0], data[2])
    # elif data[1] == '-':
    #     return math_f.sub(data[0], data[2])
    # elif data[1] == '*':
    #     return math_f.mult(data[0], data[2])
    # elif data[1] == '/':
    #     return math_f.dev(data[0], data[2])
    # else:
    #     print('something wrong')
    match data[1]:
        case '+':
            return math_f.summa(data[0], data[2])
        case '-':
            return math_f.sub(data[0], data[2])
        case '*':
            return math_f.mult(data[0], data[2])
        case '/':
            return math_f.dev(data[0], data[2])
        case _:
            print('something wrong')
