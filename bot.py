# Создать бота для вывода текущего курса валют(желательно запрос по конкретной валюте)

# /currency USD

import telebot
from cfg import TOKEN
import requests

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Курс доллара в рублях по данным ЦБ РФ {res}")

res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json() #json
for i in res.values():
        print(i)
        print(res['Valute']["USD"]['Name'], res['Valute']["USD"]['Value']) #по словарю по ключу можно вывести другую валют

bot.infinity_polling()