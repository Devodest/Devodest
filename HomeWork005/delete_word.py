# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

string = 'Мы неабв очень любим Питон иабв Джавабв'
x = 'абв'
string = string.split()
result = [item for item in string if x not in item]
print(*result)