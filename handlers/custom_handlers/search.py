from telebot.types import Message
import requests
from loader import bot
from config_data.config import RAPID_API_KEY
from states.company import CompanyInfoState
import json
from database import actions


@bot.message_handler(commands=['survey'])
def bot_search(message: Message):
    bot.send_message(message.from_user.id, 'Введите компанию или тикер для вывода информации')
    bot.set_state(message.from_user.id, CompanyInfoState.name, message.chat.id)


@bot.message_handler(state=CompanyInfoState.name)
def get_company(message: Message):

    url = "https://real-time-finance-data.p.rapidapi.com/search"
    querystring = {"query": message}
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": 'real-time-finance-data.p.rapidapi.com'
    }

    response = requests.request("GET", url, headers=headers, params=querystring, timeout=3)

    js = json.loads(response.text)

    # actions.create()

    bot.send_message(message.from_user.id, f'Основное инфо по компании:\n'
                                           f'Имя: {js.data.stock[0].name}\n'
                                           f'Цена: {js.data.stock[0].price}')
