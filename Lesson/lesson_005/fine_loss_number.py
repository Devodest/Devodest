""" 1. В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
1 2 4 5
 """
 
 
with open('file.txt', 'r') as f:
     str = f.readline()

str = str.split(' ')
str = list(map(int, str))

# for i in range(1, len(string)):
#      if string[i] - 1 != string[i-1]:
#           print(string[i] - 1)
#           break
# else:
#      print('All good')

lst = [(str[i] - 1) for i in range(1, len(str)) if str[i] - 1 != str[i-1]]
print(lst)
