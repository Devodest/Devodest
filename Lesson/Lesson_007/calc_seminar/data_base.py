path = r'cache.txt'
path_log = r'log.txt'


def save_info(a):
    a = str(a)
    with open(path, 'w') as data:
        data.write(a)


def get_info():
    with open(path, 'r') as data:
        data = data.read().split(' ')
        return data


def sve_result(a):
    a = str(a)
    with open(path, 'a') as data:
        data.write(f' = {a}')


def log(a, b):
    with open(path_log, 'a') as data:
        data.write('\nYour results: {} {} {} = {}'.format(a[0], a[1], a[2], b))
