# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# Для продвинутых - с файлом, вариант минимум - ввести позиции в консоли
# Пример -2 -1 0 1 2 Позиции: 0,1 -> 2

#НАИМЕНОВАНИЕ ФАЙЛА С ИНДЕКСАМИ == indexs.txt == (без пробелов и прочего)

print ('\tПрограмма для перемножения двух элементов списка в соответствии с индексами из файла')

print ('Для формирования списка введите число N ')
n = int(input())
new = list(range(-n, n+1))

if (n < 2):
    print ('У меня один из индексов = 4 и N меньше чем 2 ну ни как не пойдет')
    exit ()

print ('Укажите из какого файла брать индексы')
x = (input()) #  indexs.txt - без пробелов и прочего
with open(x, "r") as ind:
    ind = ind.read().split('\n')
index = list(map(int, ind))

multy = 1
for i in index:
    multy = multy * new[i]

print ('Сформирован список:')
print (new)
print ('В результате перемножения элементов с индексами:', index)
print ('Получено произведение равное:', multy)
