# import requests
#
# from config_data.config import RAPID_API_KEY
#
# import json
#
#
# url = "https://real-time-finance-data.p.rapidapi.com/search"
# querystring = {"query": 'Tesla'}
# headers = {
#     "X-RapidAPI-Key": RAPID_API_KEY,
#     "X-RapidAPI-Host": 'real-time-finance-data.p.rapidapi.com'
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring, timeout=3)
#
# print(response)
# print(response.text)
#
# js = json.loads(response.text)
#
# name = js['data']['stock'][0].get('name')
# price = js['data']['stock'][0].get('price')
#
# print(name)
# print(price)

from database import actions
from database.models import db, History

# db.create_tables([History])

db_write = actions.ActInterface.create()

data = [{"message": 'что-то' , "user": '0'}]
db_write(db, History, data)

db_read = actions.ActInterface.retrieve()

# retrieve = (db, History, History.id, History.create_at, History.message)
# print(retrieve)
# print(History.select())
# for elem in retrieve:
#     # text = text + f'elem.id elem.message \n'
#     print(elem)

with db:
    query = History.select().where(History.user == '0').order_by(History.id.desc()).limit(5)
    print(query)
    for hist in query:
        print(hist.id, hist.create_at, hist.message)

# from config_data.config import BOT_TOKEN
#
# import telebot
# from telebot import types
# token=BOT_TOKEN
# bot=telebot.TeleBot(token)
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,'Привет')
# @bot.message_handler(commands=['button'])
# def button_message(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1=types.KeyboardButton("Кнопка")
#     markup.add(item1)
#     bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
# @bot.message_handler(content_types='text')
# def message_reply(message):
#     if message.text=="Кнопка":
#         markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item1=types.KeyboardButton("Кнопка 2")
#         markup.add(item1)
#         bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
#     elif message.text=="Кнопка 2":
#         bot.send_message(message.chat.id,'Спасибо за прочтение статьи!')
# bot.infinity_polling()

# import requests
# import json
# from config_data.config import RAPID_API_KEY
#
# def func(elem: dict):
#     return (["quarter"], ["year"])
#
# url = "https://real-time-finance-data.p.rapidapi.com/company-income-statement"
# # ANNUAL QUARTERLY
# querystring = {"symbol": "Meta", "period": "QUARTERLY"}
#
# headers = {
#     "X-RapidAPI-Key": RAPID_API_KEY,
#     "X-RapidAPI-Host": "real-time-finance-data.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)
#
# js = json.loads(response.text)
#
# sorted_tuple = sorted(js['data']['income_statement'], key=lambda elem: elem['revenue'])
# print(sorted_tuple)
#
# for elem in sorted_tuple:
#     print(elem['year'], elem['quarter'], elem['revenue'])
# #

# from database.models import db, History
# from database.core import action
#
# db_write = action.create()
#
# data = [{"message": f'Инфо по бумагам Meta'}, {"user": 1535364802}]
# db_write(db, History, data)