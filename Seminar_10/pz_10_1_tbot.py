# Добавить игру, реализованную ранее, с конфетами к боту.
# Условие игры: На столе лежит 117 конфета. Играют два игрока,
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

import telebot
import requests
import datetime

from pz_10_1_config import TOKEN
bot = telebot.TeleBot(TOKEN)

# Функция, обрабатывающая команду /currency
@bot.message_handler(commands=["currency"])
def currency(message, res=False):
	bot.send_message(message.chat.id, ("Привет. Я могу предоставить тебе куры следующих валют:\n"\
	"EUR, INR, KZT, CAD, KGS, CNY, MDL, NOK, PLN, RON, XDR\n"\
	"SGD, TJS, TRY, TMT, UZS, UAH, CZK, SEK, CHF, ZAR, KRW, JPY"))
	bot.send_message(message.chat.id, "Введи обозначение валюты, чей курс ты хочешь узнать")
	bot.register_next_step_handler(message, exchange_rate)

# Функция, выводящая дату и текущий курс
def exchange_rate(message):
	pr = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
	cur = message.text
	nom = pr['Valute'][cur]['Nominal']
	name = pr['Valute'][cur]['Name']
	value = pr['Valute'][cur]['Value']
	prev = pr['Valute'][cur]['Previous']
	dt_new = datetime.datetime.now()
	bot.send_message(message.chat.id, f'{dt_new}\n {nom} {name}\n Покупка: {value} руб.  Продажа: {prev}руб.')
	bot.send_message(message.chat.id, "Введи обозначение другой валюты, чей курс ты хочешь узнать")
	bot.register_next_step_handler(message, exchange_rate)

bot.polling(none_stop=True, interval=0)

