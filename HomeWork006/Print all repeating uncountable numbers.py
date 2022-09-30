# Вывести все повторяющиеся нечётные числа

my_list = [2, 3, 5, 9, 3, 1, 5, 4, 6, 3, 2]
res = list(filter(lambda x: x % 2 == 1, my_list))
my_res = [index for index in res if res.count(index) != 1]
print(my_res)
