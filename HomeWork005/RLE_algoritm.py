# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(string):
    encoding = ''

    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + string[i]
        i += 1
    return encoding


if __name__ == '__main__':
    s = 'AABBBBCCCCDDDDDDEEEEEE'
    print(encode(s))
