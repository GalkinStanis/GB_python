# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# Собственно, это приветственная часть и ввод длины списка
print ('\tПрограмма для суммирования всх элеменетов списка стоящих на нечетных позициях')
print ('Для формирования списка введите количество элементов в списке')
n = int(input())


# Это у меня такой генератор списка целых чисел
nums = [i for i in range(0, n)]
import random
step = 0
while step < n:
    nums[step] = nums[step] + round(random.uniform (0, 20))
    step = step + 1
print("Сгенерирован список:\n", nums)


# Сам подсчет суммы
sum = 0
for i in range(len(nums)):
    if i % 2 == 1:
        sum = sum + nums[i]
print("Сумма всех элементов стоящих на нечетных позициях равна: ", sum)