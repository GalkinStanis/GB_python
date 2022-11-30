# 5'. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# Пример: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] -> [5, 7, 6, 3, 4, 2, 9, 0, 1, 8]

print ('\tПрограмма для перемешивания списка')

print ('Для формирования списка введите число N ')
n = int(input())
num_list = list(range(0, n+1))
print ("Начальный список: \n", str(num_list))

import random
for i in range(len(num_list)-1, 0, -1):
    j = random.randint(0, i + 1) 
    num_list[i], num_list[j] = num_list[j], num_list[i] 
print ("Перемешанный список: \n",  str(num_list))
