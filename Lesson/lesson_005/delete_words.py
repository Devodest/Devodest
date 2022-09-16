""" 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
'Мы неабв очень любим Питон иабв Джавабв'
'Мы очень любим Питон
 """

string = 'Мы неабв очень любим Питон иабв Джавабв'
x = 'абв'
string = string.split()
result = [item for item in string if x not in item]
print(*result)


""" for item in string:
    if not x in item:
        result.append(item)
print(*result) """