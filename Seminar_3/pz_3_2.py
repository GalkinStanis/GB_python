# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:  [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]


# Собственно, это приветственная часть и ввод длины списка
print ('\tПрограмма для перемножения элементов списка стоящих на противоположных позициях')
print ('Для формирования списка введите количество элементов в списке')
n = int(input())


# Это у меня такой генератор самого списка целых чисел
nums = [i for i in range(0, n)]
import random
step = 0
while step < n:
    nums[step] = nums[step] + int(random.uniform (0, 20))
    step = step + 1
print("Сгенерирован список:\n", nums)


# Создаем новый список, куда складываем результаты перемножения.
 
# Добавляем вначале условие, что бы при наличии нечетноко кол-ва элементов, средний * сам на себя
if n/2 %2 == 1:
    temp = int(n/2)
else:
    temp = int(n/2) + 1

# Собственно сам список произведений
multy = [int(nums[i]) * int(nums[-i-1]) for i in range(0, temp)]
print("Список полученый в результате перемножения:\n", multy)
