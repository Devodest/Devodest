
path = r'data.txt'


def save_info(a):
    a = str(a)
    with open(path, 'w') as data:
        data.write(a)


def get_info():
    with open(path, 'r') as data:
        data = data.read().split(' ')
        return data
