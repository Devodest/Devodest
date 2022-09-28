# " 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число 7.
# ['65h34q', 'sdg634d', '147jnbv']
incoming_list = ['65h34q', 'sdg634d', '147jnbv']
find_something = '6'
out_coming_list = [index for index in incoming_list if find_something in index]
print(out_coming_list)
