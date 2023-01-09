# Добавить игру, реализованную ранее, с конфетами к боту.
# Условие игры: На столе лежит 117 конфета. Играют два игрока,
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

import telebot
import random
from pz_9_1_config import TOKEN
bot = telebot.TeleBot(TOKEN)

remains = 117

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
	bot.send_message(message.chat.id, ("Привет.\n Предлагаю сыграть в игру.\n"\
	"На столе лежит 117 конфет. Я буду играть против тебя.\n "\
	"Первый ход определяется жеребьёвкой.\n За один ход можно забрать не более"\
	" чем 28 конфет. \n Все конфеты оппонента достаются сделавшему последний ход.\n"\
	" Если готов - то отправь 'y'")) # не смог сделать автоматический переход на следующий метод. Только при отправлении запроса
	bot.next_step_handler(message, starting_number)

# метод для жеребьевки
def starting_number(message):
	if int(random.uniform (1, 2)) ==1:
		bot.send_message(message.chat.id, "Моя жеребьевка показывает, что первый ход твой.")
		bot.send_message(message.chat.id, "Возьми со стола от 1 до 28 конфет")	
		bot.next_step_handler(message, my_step) 
	else:
		bot.send_message(message.chat.id, "Моя жеребьевка показывает, что первый ход мой")
		bot.send_message(message.chat.id, "Если хочешь, что бы я походил, нажми 'y'")
		# не смог сделать автоматический переход на следующий метод. Только при отправлении запроса
		bot.next_step_handler(message, step_bot)

# метод для хода игрока
def my_step(message):
	sweets1 = int(message.text)
	norma = 28
	global remains
	remains = remains - sweets1
	bot.send_message(message.chat.id, f'Ты взял {sweets1} конфеты.\n Осталось {remains} конфет')
	if remains > norma:
		bot.send_message(message.chat.id, "Если хочешь, что бы я походил, нажми 'y'")
		# не смог сделать автоматический переход на следующий метод. Только при отправлении запроса
		bot.next_step_handler(message, step_bot)
	else:
		bot.send_message(message.chat.id, "Отлично. Я выйграл")		
		
# метод для хода бота
def step_bot(message):
	norma = 28
	global remains
	temp = int(remains % norma)
	if temp > 1: sweets2 = temp - 1
	if temp == 1 and (remains / norma) %2 == 0 : sweets2 = 28
	if temp == 1 and (remains / norma) %2 != 0 : sweets2 = int(random.uniform (1, 29))
	remains = remains - sweets2
	bot.send_message(message.chat.id, f'Я взял {sweets2} конфеты.\n Осталось {remains} конфет')
	if remains > norma:
		bot.send_message(message.chat.id, "Возьми со стола от 1 до 28 конфет")	
		bot.next_step_handler(message, my_step) 
	else: 
		bot.send_message(message.chat.id, "Отвратительно. Ты выйграл")

bot.polling(none_stop=True, interval=0)