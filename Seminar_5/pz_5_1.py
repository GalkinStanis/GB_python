# 1. Создайте программу для игры с конфетами человек против человека.  Добавьте игру против простого и умного ботов
# *' Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.


#  Человек - Человек
#  Приветственная часть м ввод игроков
print ('\tИгра с конфетами Чеолвек против Человека')
print ('Введите имя участника')
name_i = (input())
print ('Введите имя другого участника')
name_j = (input())
#  Определение очередности хода
import random
n =  int(random.uniform (1, 3))
if n == 1:
    name_1 = name_i
    name_2 = name_j
else:
    name_1 = name_j
    name_2 = name_i

#  Условия игры, начальное кол-во конфет и сколько можно максимум брать за раз
remains = int(117)
norma = int(28)

#  Вывод условий на экран
print("\nНа столе лежит",remains, "конфет. Участники по очереди берут конфеты. За один раз можно взять не более 28 конфет.")
print("Пропускать ход или брать 0 конфет нельзя. Выйграл тот учостник, после хода которого на столе не останется конфет.")

#  Сама игра
while remains > 0:
    for i in [name_1, name_2]:
        print ('\nСейчас', i, 'берет конфеты. нужно взять больше чем 0, но не больше чем 28')
        sweets = int(input())
        remains = remains - sweets
        if remains == 0:
            print ('Поздравляю',i,'Ты выйграл!!!')
            exit() 
        else:
            print("В остатке осталось", remains, "конфет")



# #  Человек - Бот
# #  Приветственная часть м ввод игроков
# print ('\tИгра с конфетами Чеолвек против Бота')
# print ('Введите своё имя')
# name_i = (input())
# name_j = ('Бот')

# #  Определение очередности хода
# import random
# n =  int(random.uniform (1, 3))
# if n == 1:
#     name_1 = name_i
#     name_2 = name_j
# else:
#     name_2 = name_i
#     name_1 = name_j

# #  Условия игры, начальное кол-во конфет и сколько можно максимум брать за раз
# remains = int(117)
# norma = int(28)

# #  Вывод условий на экран
# print("\nНа столе лежит",remains, "конфет. Участники по очереди берут конфеты. За один раз можно взять не более 28 конфет.")
# print("Пропускать ход или брать 0 конфет нельзя. Выйграл тот учостник, после хода которого на столе не останется конфет.")

# #  Сама игра
# while remains > 0:
#     for i in [name_1, name_2]:
#         print ('\nСейчас', i, 'берет конфеты. нужно взять больше чем 0, но не больше чем 28')
#         if i == 'Бот':
#             if remains > norma:
#                 sweets = int(random.uniform (1, 29))
#             else: 
#                 sweets = remains
#             print ('Бот забрал',sweets,'конфет')
#         else:
#             sweets = int(input())
#         remains = remains - sweets
#         if remains == 0:
#             print ('Поздравляю',i,'. Ты выйграл!!!')
#             exit() 
#         else:
#             print("В остатке осталось", remains, "конфет")




# #  Человек - Умный бот
# #  Приветственная часть м ввод игроков
# print ('\tИгра с конфетами Чеолвек против Умного бота')
# print ('Введите своё имя')
# name_i = (input())
# name_j = ('Умник')

# #  Определение очередности хода
# import random
# n =  int(random.uniform (1, 3))
# if n == 1:
#     name_1 = name_i
#     name_2 = name_j
# else:
#     name_2 = name_i
#     name_1 = name_j

# #  Условия игры, начальное кол-во конфет и сколько можно максимум брать за раз
# remains = int(117)
# norma = int(28)

# #  Вывод условий на экран
# print("\nНа столе лежит",remains, "конфет. Участники по очереди берут конфеты. За один раз можно взять не более 28 конфет.")
# print("Пропускать ход или брать 0 конфет нельзя. Выйграл тот учостник, после хода которого на столе не останется конфет.")

# #  Сама игра
# while remains > 0:
#     for i in [name_1, name_2]:
#         print ('\nСейчас', i, 'берет конфеты. нужно взять больше чем 0, но не больше чем 28')
#         if i == 'Умник':
#             if remains > norma:
#                 sweets = remains % (norma + 1)
#             else: 
#                 sweets = remains
#             print ('Умник забрал',sweets,'конфет')
#         else:
#             sweets = int(input())
#         remains = remains - sweets
#         if remains == 0:
#             print ('Поздравляю',i,'. Ты выйграл!!!')
#             exit() 
#         else:
#             print("В остатке осталось", remains, "конфет")